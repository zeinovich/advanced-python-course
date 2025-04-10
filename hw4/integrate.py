import math
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate_chunk(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_type="thread"):
    chunk_size = n_iter // n_jobs
    futures = []
    step = (b - a) / n_jobs
    Executor = (
        ThreadPoolExecutor
        if executor_type == "thread"
        else ProcessPoolExecutor
    )

    with Executor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            chunk_a = a + i * step
            chunk_b = a + (i + 1) * step
            futures.append(
                executor.submit(
                    integrate_chunk, f, chunk_a, chunk_b, chunk_size
                )
            )
        result = sum(f.result() for f in futures)
    return result


if __name__ == "__main__":
    cpu_count = os.cpu_count()
    print(f"{cpu_count=}")
    results = []
    for n in range(1, cpu_count * 2 + 1):
        start_t = time.perf_counter()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n, executor_type="thread")
        thread_time = time.perf_counter() - start_t

        start_p = time.perf_counter()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n, executor_type="process")
        process_time = time.perf_counter() - start_p

        results.append((n, thread_time, process_time))

    with open("./hw4/artifacts/integrate_times.txt", "w") as f:
        f.write(f"{os.cpu_count()=}\n")
        f.write("n_jobs\tThreadPoolExecutor\tProcessPoolExecutor\n")
        for n, t_time, p_time in results:
            f.write(f"{n}\t{t_time:.4f}\t{p_time:.4f}\n")
