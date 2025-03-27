import numpy as np

from matlib_hash import Matrix

if __name__ == "__main__":
    np.random.seed(0)
    A = Matrix(np.random.randint(0, 10, (10, 10)))
    B = Matrix(np.random.randint(0, 10, (10, 10)))
    C = Matrix(A.data.copy())

    # This will create collision because sum is kept unchanged
    C.data[0, 0] += 1
    C.data[0, 1] -= 1

    assert hash(A) == hash(C)

    D = Matrix(B.data.copy())

    A.save_to_file("./hw3/artifacts/A.txt")
    B.save_to_file("./hw3/artifacts/B.txt")
    C.save_to_file("./hw3/artifacts/C.txt")
    D.save_to_file("./hw3/artifacts/D.txt")

    AB = A @ B
    CD = C @ D

    AB.save_to_file("./hw3/artifacts/AB.txt")
    CD.save_to_file("./hw3/artifacts/CD.txt")

    with open("./hw3/artifacts/hash.txt", "w") as f:
        f.write(f"hash(AB): {hash(AB)}\nhash(CD): {hash(CD)}")
