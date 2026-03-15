"""Minify CSS files for production.

Usage: python scripts/minify_css.py
"""

import glob
import os

import rcssmin

CSS_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "static")


def minify():
    for path in glob.glob(os.path.join(CSS_DIR, "*.css")):
        if path.endswith(".min.css"):
            continue
        with open(path) as f:
            original = f.read()
        minified = rcssmin.cssmin(original)
        saved = len(original) - len(minified)
        pct = (saved / len(original)) * 100 if original else 0
        with open(path, "w") as f:
            f.write(minified)
        print(f"  {os.path.basename(path)}: {len(original)} → {len(minified)} bytes ({pct:.1f}% reduction)")


if __name__ == "__main__":
    minify()
