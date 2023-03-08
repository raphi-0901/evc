from typing import Tuple
import numpy as np

A = 1
B = 2
C = 2
D = 2
E = 0
F = 8
G = 3
H = 6


def define_structures() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
        Defines the two vectors v1 and v2 as well as the matrix M determined by your matriculation number.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    v1 = np.array([D, A, C])
    v2 = np.array([F, B, E])
    M = np.array([[D, B, C], [B, G, A], [E, H, F]])
    # END STUDENT CODE

    return v1, v2, M


def sequence(M: np.ndarray) -> np.ndarray:
    """
        Defines a vector given by the minimum and maximum digit of your matriculation number. Step size = 0.25.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    min = np.ndarray.min(M)
    max = np.ndarray.max(M)
    step = 0.25
    # arange does not include the end value,
    # so by adding the step to the max value
    # I make sure the max is included in result
    result = np.arange(min, max + step, step)

    # END STUDENT CODE

    return result


def matrix(M: np.ndarray) -> np.ndarray:
    """
        Defines the 15x9 block matrix as described in the task description.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    zeros = np.zeros((3, 3))
    r = np.zeros((15, 9))
    firstRow = np.hstack((M, zeros, M))
    secondRow = np.hstack((zeros, M, zeros))
    r = np.vstack((firstRow, secondRow, firstRow, secondRow, firstRow))

    # END STUDENT CODE

    return r


def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
    """
        Dot product of v1 and v2.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    if v1.shape != v2.shape:
        return 0

    r = 0

    for i in range(v1.shape[0]):
        r += v1[i] * v2[i]

    # END STUDENT CODE
    return r


def cross_product(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """
        Cross product of v1 and v2.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros(v1.shape)

    if v1.shape != v2.shape:
        return r

    # append the first two elemts to the bottom of the arrays
    # this allows us to iterate easily over the array and do our calculations
    extendedV1 = np.hstack((v1, [v1[i] for i in range(len(v1) - 1)]))
    extendedV2 = np.hstack((v2, [v2[i] for i in range(len(v2) - 1)]))

    for i in range(extendedV1.shape[0] - 2):
        r[i] = extendedV1[i + 1] * extendedV2[i + 2] - \
            extendedV1[i + 2] * extendedV2[i + 1]
    # END STUDENT CODE

    return r


def vector_X_matrix(v: np.ndarray, M: np.ndarray) -> np.ndarray:
    """
        Defines the vector-matrix multiplication v*M.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    r = np.zeros((v.shape[0]))
    for i in range(v.shape[0]):
        r[i] = dot_product(np.ndarray.transpose(M[i]), v)

    # END STUDENT CODE
    return r


def matrix_X_vector(M: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
        Defines the matrix-vector multiplication M*v.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros((v.shape[0]))

    for i in range(v.shape[0]):
        r[i] = dot_product(v, np.ndarray.transpose(M)[i])

    # END STUDENT CODE
    return r


def matrix_X_matrix(M1: np.ndarray, M2: np.ndarray) -> np.ndarray:
    """
        Defines the matrix multiplication M1*M2.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    r = np.zeros((M1.shape[0], M2.shape[1]))
    for i in range(M1.shape[0]):
        for j in range(M2.shape[1]):
            r[i][j] = dot_product(M1[i], np.ndarray.transpose(M2)[j])
    # END STUDENT CODE

    return r


def matrix_Xc_matrix(M1: np.ndarray, M2: np.ndarray) -> np.ndarray:
    """
        Defines the element-wise matrix multiplication M1*M2 (Hadamard Product).
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros(M1.shape)

    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            r[i][j] = M1[i][j] * M2[i][j]
    # END STUDENT CODE

    return r
