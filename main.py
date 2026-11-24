"""Write Nur's genuine make.fun handle to entry.txt.

Writes exactly "nuraliana-ana" (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

ENTRY = "nuraliana-ana"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
