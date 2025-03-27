import numpy as np


class SaveMixin:
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


class DisplayMixin:
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])


class PropertyMixin:
    @property
    def shape(self):
        return self.data.shape

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        if not all(len(row) == len(new_data[0]) for row in new_data):
            raise ValueError("All rows must have the same length")
        self._data = np.array(new_data)


class Matrix(SaveMixin, DisplayMixin, PropertyMixin):
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length")
        self.data = np.array(data)
        self.shape = self.data.shape

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError(
                "Matrices must have the same dimensions for addition"
            )
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError(
                "Matrices must have the same dimensions for element-wise multiplication"
            )
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Invalid matrix dimensions for multiplication")
        return Matrix(self.data @ other.data)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])
