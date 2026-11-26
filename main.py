"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single one-line excuse, under 140 characters, to
``<output-dir>/entry.txt``. Pure standard library, deterministic:
the same line every run, no clock, no randomness, no network.
"""

import os
import shutil

LINE = "All green. Turns out the tests were testing the tests, and the product was just there for moral support."


def main():
    # The gate requires 1 to 140 characters of UTF-8 text, not only
    # whitespace; fail loudly here rather than hand in an invalid line.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise SystemExit("entry line must be 1-140 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The grader owns the output directory: clear only its contents,
    # never the directory itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
