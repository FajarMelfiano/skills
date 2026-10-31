#!/usr/bin/env python3
"""Import SKILL.md skills from a GitHub repo into ~/workspace/skills.

Safety screening runs on every SKILL.md before copying. Heuristic only:
high-risk hits still need human review.
"""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

DEST = os.path.expanduser("~/workspace/skills")

SUSPICIOUS = [
    (r"ignore (all |any )?previous instructions", "prompt-injection phrase"),
    (r"disregard (all |any )?(prior|previous) instructions", "prompt-injection phrase"),
    (r"you are (now|actually)", "possible role hijack"),
    (r"exfiltrat", "possible data exfiltration"),
    (r"send .* to (a |an )?(remote|external|third)", "possible data exfiltration"),
    (r"curl[^\n|]*\|\s*(ba)?sh", "piped remote code execution"),
    (r"wget[^\n|]*\|\s*(ba)?sh", "piped remote code execution"),
    (r"rm\s+-rf\s+/( |$)", "destructive command"),
    (r":\(\)\s*\{\s*:\|\:&\s*\}", "fork bomb"),
    (r"(api[_-]?key|secret[_-]?key|private[_-]?key)\s*[:=]", "credential harvesting"),
    (r"system prompt", "tries to reveal/override system prompt"),
]


def find_skill_dirs(root):
    found = []
    for dirpath, _dirnames, filenames in os.walk(root):
        if ".git" in dirpath:
            continue
        if "SKILL.md" in filenames:
            found.append(dirpath)
    return sorted(found)


def read_frontmatter_name(skill_md):
    try:
        with open(skill_md, encoding="utf-8") as f:
            head = f.read(2000)
    except OSError:
        return None
    m = re.search(r"^---\s*\n(.*?)\n---", head, re.S)
    if not m:
        return None
    n = re.search(r"^name:\s*[\"']?([^\"'\n]+)[\"']?", m.group(1), re.M)
    return n.group(1).strip() if n else None


def screen(skill_dir):
    hits = []
    for dirpath, _dn, filenames in os.walk(skill_dir):
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8", errors="ignore") as f:
                    text = f.read()
            except OSError:
                continue
            for pattern, label in SUSPICIOUS:
                if re.search(pattern, text, re.I):
                    hits.append("%s in %s" % (label, os.path.relpath(p, skill_dir)))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="GitHub repo URL to clone")
    ap.add_argument("--subdir", default="", help="Subdirectory inside repo to scan")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="Overwrite existing skills")
    args = ap.parse_args()

    tmp = tempfile.mkdtemp(prefix="skillimport-")
    try:
        r = subprocess.run(
            ["git", "clone", "--depth", "1", "-q", args.repo, tmp + "/repo"],
            capture_output=True, text=True)
        if r.returncode != 0:
            print("clone failed:", r.stderr.strip()[:300], file=sys.stderr)
            return 1
        root = os.path.join(tmp, "repo", args.subdir)
        if not os.path.isdir(root):
            print("subdir not found:", args.subdir, file=sys.stderr)
            return 1

        imported, skipped, rejected = [], [], []
        seen_hashes = {}
        for sdir in find_skill_dirs(root):
            skill_md = os.path.join(sdir, "SKILL.md")
            name = read_frontmatter_name(skill_md) or os.path.basename(sdir)
            try:
                with open(skill_md, "rb") as f:
                    h = hashlib.sha256(f.read()).hexdigest()[:16]
            except OSError:
                h = None
            if h and h in seen_hashes:
                skipped.append((name, "duplicate content of " + seen_hashes[h]))
                continue
            dest = os.path.join(DEST, name)
            if os.path.exists(dest) and not args.force:
                skipped.append((name, "already exists"))
                continue
            hits = screen(sdir)
            if hits:
                rejected.append((name, hits))
                continue
            if not args.dry_run:
                if os.path.exists(dest):
                    shutil.rmtree(dest)
                shutil.copytree(sdir, dest)
            imported.append(name)
            if h:
                seen_hashes[h] = name

        print("== would import ==" if args.dry_run else "== imported ==")
        for n in imported:
            print(" +", n)
        print("== skipped ==")
        for n, why in skipped:
            print(" -", n, "(%s)" % why)
        print("== rejected (needs manual review) ==")
        for n, hits in rejected:
            print(" !", n)
            for h in hits:
                print("    -", h)
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
