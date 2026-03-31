#!/usr/bin/env python3
"""Map local image files to publication preview filenames using fuzzy token matching.

Usage:
  python3 bin/map_preview_images.py --source /path/to/images --apply
  python3 bin/map_preview_images.py --source /path/to/images --threshold 0.30

Default mode is dry-run and prints proposed matches.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "assets" / "img" / "publication_preview" / "manifest.csv"
TARGET_DIR = ROOT / "assets" / "img" / "publication_preview"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".tif", ".tiff"}
STOP = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "using",
    "of",
    "in",
    "to",
    "a",
    "an",
    "by",
    "on",
    "at",
    "mr",
    "mri",
    "study",
    "image",
    "images",
    "figure",
}


def norm_tokens(text: str) -> set[str]:
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return {t for t in tokens if len(t) > 2 and t not in STOP}


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def score(source_name: str, title: str, key: str) -> float:
    src = norm_tokens(source_name)
    tgt = norm_tokens(title + " " + key)
    if not src or not tgt:
        return 0.0
    overlap = len(src & tgt)
    return overlap / max(len(src), 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Directory containing candidate images")
    parser.add_argument("--threshold", type=float, default=0.33, help="Minimum score to accept a match")
    parser.add_argument("--apply", action="store_true", help="Copy matched files into publication_preview")
    args = parser.parse_args()

    source_dir = Path(args.source).expanduser().resolve()
    if not source_dir.exists() or not source_dir.is_dir():
        raise SystemExit(f"Source directory does not exist: {source_dir}")
    if not MANIFEST.exists():
        raise SystemExit(f"Manifest not found: {MANIFEST}. Run generate_preview_manifest.py first.")

    rows = read_manifest(MANIFEST)
    candidates = [p for p in source_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS]

    if not candidates:
        raise SystemExit("No image files found in source directory.")

    matched = 0
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    for row in rows:
        best = None
        best_score = 0.0
        for cand in candidates:
            s = score(cand.stem, row.get("title", ""), row.get("key", ""))
            if s > best_score:
                best_score = s
                best = cand

        if not best or best_score < args.threshold:
            print(f"NO MATCH  {row.get('preview','')}  score<{args.threshold:.2f}")
            continue

        matched += 1
        dst = TARGET_DIR / row["preview"]
        print(f"MATCH     {best.name} -> {row['preview']}  (score={best_score:.2f})")
        if args.apply:
            shutil.copy2(best, dst)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"{mode}: matched {matched}/{len(rows)} publications")


if __name__ == "__main__":
    main()
