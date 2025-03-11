import sys


def count_stats(file):
    lines, words, bytes_ = 0, 0, 0
    for line in file:
        lines += 1
        words += len(line.split())
        bytes_ += len(line.encode("utf-8"))
    return lines, words, bytes_


def print_stats(stats, filename=""):
    print(f"{stats[0]:7} {stats[1]:7} {stats[2]:7} {filename}")


if __name__ == "__main__":
    total = [0, 0, 0]

    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "r", encoding="utf-8") as f:
                stats = count_stats(f)
                print_stats(stats, filename)
                total = [t + s for t, s in zip(total, stats)]

        if len(sys.argv) > 2:
            print_stats(total, "total")
    else:
        stats = count_stats(sys.stdin)
        print_stats(stats)
