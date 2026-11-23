import os
import shutil

# Copy the pre-written entry to the output directory.
# Standard library only: no third-party imports, no network, no writes
# into this directory. The grader runs this program with
# MAKEFUN_OUTPUT_DIR set to a writable directory.
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.txt"), os.path.join(OUT, "entry.txt"))
    print("wrote %s" % os.path.join(OUT, "entry.txt"))


if __name__ == "__main__":
    main()
