                            #!/usr/bin/env python3
"""Extract embedded images from DOCX files.

Input folder: data/docx_summary_inbox
Output folder: data/docx_extracted_images/<docx_stem>/
"""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "data" / "docx_summary_inbox"
OUT = ROOT / "data" / "docx_extracted_images"

VALID_EXT = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".webp"}


def main() -> None:
    INBOX.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    docx_files = sorted(INBOX.glob("*.docx"))
    if not docx_files:
        print(f"No DOCX files found in {INBOX}")
        return

    total = 0
    for docx in docx_files:
        dest = OUT / docx.stem
        dest.mkdir(parents=True, exist_ok=True)

        count = 0
        with zipfile.ZipFile(docx, "r") as zf:
            for name in zf.namelist():
                if not name.startswith("word/media/"):
                    continue
                ext = Path(name).suffix.lower()
                if ext not in VALID_EXT:
                    continue
                count += 1
                target = dest / f"img_{count:03d}{ext}"
                with zf.open(name) as src, target.open("wb") as out:
                    out.write(src.read())

        total += count
        print(f"{docx.name}: extracted {count} images -> {dest}")

    print(f"Done. Extracted {total} images from {len(docx_files)} DOCX files.")


if __name__ == "__main__":
    main()
