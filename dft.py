# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import numpy as np
from numpy.random import rand

class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        dft_matrix = matrix
        dft_matrix = np.asarray(dft_matrix, dtype=complex)

        rows, cols = matrix.shape
        # rows = len(matrix)
        # cols = len(matrix[0])

        for u in range(rows):
            for v in range(cols):
                # value = np.dtype('int64').type(z)
                value = 0 + 0j
                for row in range(rows):
                    for col in range(cols):
                        value += matrix[row][col]*np.exp(-2j*np.pi*(row*u + col*v)/cols)

                dft_matrix[u][v] = value

        return dft_matrix

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""

        idft_matrix = matrix
        idft_matrix = np.asarray(idft_matrix, dtype=complex)

        rows, cols = matrix.shape
        # rows = len(matrix)
        # cols = len(matrix[0])

        for u in range(rows):
            for v in range(cols):
                # value = np.dtype('int64').type(z)
                value = 0 + 0j
                for row in range(rows):
                    for col in range(cols):
                        value += matrix[row][col] * np.exp(2j * np.pi * (row * u + col * v) / cols) / (cols**2)

                idft_matrix[u][v] = value

        return idft_matrix

    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""

        return abs(matrix)


