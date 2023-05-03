from typing import List, Tuple

import numpy as np

A = 1
B = 2
C = 2
D = 2
E = 0
F = 8
G = 3
H = 6


def define_triangle() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    P1 = [1+C, -(1+A), -(1+E)]
    P2 = [-(1+G), -(1+B), -(1+H)]
    P3 = [-(1+D), 1+F, -(1+B)]
    # END STUDENT CODE

    return P1, P2, P3


def define_triangle_vertices(P1: np.ndarray, P2: np.ndarray, P3: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    P1P2 = np.subtract(P2, P1)
    P2P3 = np.subtract(P3, P2)
    P3P1 = np.subtract(P1, P3)
    # END STUDENT CODE

    return P1P2, P2P3, P3P1


def compute_lengths(P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray) -> List[float]:
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    sumP1P2 = 0
    sumP2P3 = 0
    sumP3P1 = 0
    for i in range(len(P1P2)):
        sumP1P2 += P1P2[i] ** 2

    for i in range(len(P2P3)):
        sumP2P3 += P2P3[i] ** 2

    for i in range(len(P3P1)):
        sumP3P1 += P3P1[i] ** 2

    norms = [sumP1P2 ** 0.5, sumP2P3 ** 0.5, sumP3P1 ** 0.5]
    # END STUDENT CODE

    return norms


def compute_normal_vector(P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    distanceAB = np.subtract(P1P2, P2P3)
    distanceAC = np.subtract(P1P2, P3P1)

    n = np.cross(distanceAC, distanceAB)
    n_normalized = (1 / np.linalg.norm(n)) * n
    # END STUDENT CODE

    return n, n_normalized


def compute_triangle_area(n: np.ndarray) -> float:
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    area = np.linalg.norm(n) / 2
    # END STUDENT CODE

    return area


def calculate_angle(v1, v2):
    # formel für winkel:
    # (a * b) / |a| * |b|

    # von radiant in grad umrechnen:
    # 180°/PI * Winkel in Grad

    return 180 - (np.arccos(np.dot(v1, v2) /
                            (np.linalg.norm(v1) * np.linalg.norm(v2)))) * 180/np.pi


def compute_angles(P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray) -> Tuple[float, float, float]:
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    alpha = calculate_angle(P1P2, P3P1)
    beta = calculate_angle(P1P2, P2P3)
    gamma = calculate_angle(P2P3, P3P1)
    # END STUDENT CODE

    return alpha, beta, gamma
