import numpy as np
from matlib import Matrix

if __name__ == "__main__":
    np.random.seed(0)
    mat1 = Matrix(np.random.randint(0, 10, (10, 10)))
    mat2 = Matrix(np.random.randint(0, 10, (10, 10)))

    with open("./hw3/artifacts/matrix+.txt", "w") as f:
        f.write(str(mat1 + mat2))

    with open("./hw3/artifacts/matrix*.txt", "w") as f:
        f.write(str(mat1 * mat2))

    with open("./hw3/artifacts/matrix@.txt", "w") as f:
        f.write(str(mat1 @ mat2))
