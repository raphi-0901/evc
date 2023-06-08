# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

from typing import List
import numpy as np


class ClippingPlane:

    def __init__(self, plane: np.ndarray):
        """ plane     ... plane stored in Hessian normal form as a 1x4 vector"""
        self.plane = plane

    def inside(self, pos: np.ndarray) -> bool:
        """Checks if a given point lies behind the plane (opposite direction
        of normal vector). Points lying on the plane are considered to be
        inside.
        position  ... homogeneous position with 4 components
        return res... logical value which indicates if the point is
                      inside or not """

        # STUDENT CODE
        # TODO 2: Implement this function.
        # HINT:   You can access the plane property via self.plane.
        # NOTE:   The following lines can be removed. They prevent the framework
        #         from crashing.

        # innerhalb wenn Skalarprodukt < 0
        # außerhalb wenn Skalarprodukt > 0
        # darauf wenn Skalarprodukt = 0
        res = np.dot(pos, self.plane) <= 0

        # END STUDENT CODE

        return res

    def intersect(self, pos1: np.ndarray, pos2: np.ndarray) -> float:
        """Intersects the plane with a line between pos1 and pos2.
        pos1      ... homogeneous position with 4 components
        pos2      ... homogeneous position with 4 components
        return t  ... normalized intersection value t in [0, 1]"""

        # STUDENT CODE
        la = np.dot(pos1, self.plane)
        lb = np.dot(pos2, self.plane)
        t = la / (la - lb)
        t = max(0.0, min(t, 1.0))

        # END STUDENT CODE
        return t

    @staticmethod
    def get_clipping_planes() -> List:
        """creates and returns a list of the six Clipping planes defined in the task description."""

        # STUDENT CODE
        # TODO 2: Define the correct clip planes.
        # NOTE:   The following lines can be removed. They prevent the framework
        #         from crashing.

        # Eine Ebene p⃗ wird in Hessescher Normalform4 dargestellt und kann damit in einem 4-Komponenten
        # Vektor gespeichert werden, wobei die ersten drei Komponenten dem Normalvektor (Richtung) der Ebe-
        # ne und die letzte der negativen Distanz zum Ursprung entspricht

        left_plane = ClippingPlane(np.array([1, 0, 0, -1]))
        right_plane = ClippingPlane(np.array([-1, 0, 0, -1]))
        bottom_plane = ClippingPlane(np.array([0, 1, 0, -1]))
        top_plane = ClippingPlane(np.array([0, -1, 0, -1]))
        near_plane = ClippingPlane(np.array([0, 0, 1, -1]))
        far_plane = ClippingPlane(np.array([0, 0, -1, -1]))

        res = [
            left_plane, right_plane, bottom_plane, top_plane, near_plane, far_plane
        ]

        # END STUDENT CODE

        return res
