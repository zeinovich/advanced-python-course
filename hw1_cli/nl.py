import sys


def number_lines(file):
    for i, line in enumerate(file, start=1):
        print(f"{i}\t{line.rstrip()}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            number_lines(f)
    else:
        number_lines(sys.stdin)
