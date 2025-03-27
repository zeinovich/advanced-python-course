import numpy as np

from matlib_mixins import Matrix

if __name__ == "__main__":
    np.random.seed(0)
    mat1 = Matrix(np.random.randint(0, 10, (10, 10)))
    mat2 = Matrix(np.random.randint(0, 10, (10, 10)))

    (mat1 + mat2).save_to_file("./hw3/artifacts/mixins-matrix+.txt")
    (mat1 - mat2).save_to_file("./hw3/artifacts/mixins-matrix-.txt")
    (mat1 * mat2).save_to_file("./hw3/artifacts/mixins-matrix*.txt")
    (mat1 / (mat2 + Matrix(np.ones((10, 10))))).save_to_file(
        "./hw3/artifacts/mixins-matrix_div.txt"
    )
    (mat1 @ mat2).save_to_file("./hw3/artifacts/mixins-matrix@.txt")
