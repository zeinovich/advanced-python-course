import sys

NUM_LINES_DEFAULT = 10
NUM_LINES_STDIN = 17


def tail(file, num_lines):
    lines = file.readlines()
    for line in lines[-num_lines:]:
        print(line, end="")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, filename in enumerate(sys.argv[1:]):
            if len(sys.argv) > 2:
                print(f"==> {filename} <==")

            with open(filename, "r", encoding="utf-8") as f:
                tail(f, NUM_LINES_DEFAULT)
                if i < len(sys.argv) - 2:
                    print()
    else:
        tail(sys.stdin, NUM_LINES_STDIN)
