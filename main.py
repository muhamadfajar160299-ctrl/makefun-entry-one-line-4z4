"""Copy the bundled one-liner to the grader output directory.

Reads entry.txt next to this file and writes it, byte for byte, to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt) with mode 0644,
so the grader can read it. Single direct write, no temp file.
"""

import os
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        pass
    out = out_dir / "entry.txt"
    out.write_bytes(text)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
