#!/usr/bin/env python3
"""
tools/svgs_to_pptx.py

Converts a directory of slide SVGs to a native DrawingML PPTX.
This is the PPT Master post-processing step — run AFTER Claude has written
all SVG files directly to svg_output/.

Usage:
    python3 tools/svgs_to_pptx.py <svg_output_dir> [output.pptx]

Example:
    python3 tools/svgs_to_pptx.py slide_deck_template/decks/sql-joins/svg_output

Requires:
    pip3 install python-pptx Pillow
"""

from __future__ import annotations

import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

from svg_to_pptx import create_pptx_with_native_svg  # noqa: E402


def convert(svg_dir: str, out_path: str | None = None) -> str:
    svg_dir_path = Path(svg_dir)
    if not svg_dir_path.is_dir():
        print(f"ERROR: SVG directory not found: {svg_dir}")
        sys.exit(1)

    svg_files = sorted(svg_dir_path.glob("slide*.svg"))
    if not svg_files:
        print(f"ERROR: No slide*.svg files found in {svg_dir}")
        sys.exit(1)

    if not out_path:
        # Default: sibling of svg_output/ dir, named after parent folder
        out_path = str(svg_dir_path.parent / f"{svg_dir_path.parent.name}.pptx")

    print(f"Converting {len(svg_files)} SVGs → {Path(out_path).name}")

    ok = create_pptx_with_native_svg(
        svg_files=svg_files,
        output_path=Path(out_path),
        canvas_format="ppt169",
        verbose=True,
        transition="fade",
        use_compat_mode=False,
        use_native_shapes=True,
        enable_notes=False,
    )

    if ok:
        size_kb = Path(out_path).stat().st_size // 1024
        print(f"\noutput_path: {out_path}  ({size_kb} KB)")
    else:
        print("\nERROR: Conversion reported failures — check output above.")
        sys.exit(1)

    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/svgs_to_pptx.py <svg_output_dir> [output.pptx]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
