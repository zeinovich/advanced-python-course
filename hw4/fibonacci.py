import time
import threading
import multiprocessing


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def run_sync(n, count):
    start = time.perf_counter()
    for _ in range(count):
        fib(n)
    end = time.perf_counter()
    return end - start


def run_threads(n, count):
    threads = []
    start = time.perf_counter()
    for _ in range(count):
        t = threading.Thread(target=fib, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.perf_counter()
    return end - start


def run_processes(n, count):
    processes = []
    start = time.perf_counter()
    for _ in range(count):
        p = multiprocessing.Process(target=fib, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    N = 35
    COUNT = 10

    sync_time = run_sync(N, COUNT)
    thread_time = run_threads(N, COUNT)
    process_time = run_processes(N, COUNT)

    with open("./hw4/artifacts/fib_times.txt", "w") as f:
        f.write(f"Sync: {sync_time:.2f} seconds\n")
        f.write(f"Threads: {thread_time:.2f} seconds\n")
        f.write(f"Processes: {process_time:.2f} seconds\n")
