# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

import numpy as np
from numpy.matlib import repmat

from MeshVertex import MeshVertex
from Framebuffer import Framebuffer
from MeshVertex import MeshVertex


def fill_rasterization(mesh: MeshVertex, framebuffer: Framebuffer):
    """ applies the fill rasterization algorithm. Draws a mesh to the Framebuffer."""

    for i in range(mesh.faces.shape[0]):
        v1 = mesh.get_face(i).get_vertex(0)
        for j in range(mesh.faces[i][0]-1):
            i, j = np.array(i).reshape(np.asarray(i).size), np.array(
                j).reshape(np.asarray(j).size)

            v2 = mesh.get_face(i).get_vertex(j)
            v3 = mesh.get_face(i).get_vertex(j+1)
            draw_triangle(framebuffer, v1, v2, v3)


def line_eq(A: float, B: float, C: float, x: float, y: float) -> float:
    """defines the line equation described by the provided parameters and
        returns the distance of a point (x, y) to this line.
        A    ... line equation parameter 1
        B    ... line equation parameter 2
        C    ... line equation parameter 3
        x    ... x coordinate of point to test against the line
        y    ... y coordinate of point to test against the line
        res  ... distance of the point (x, y) to the line (A, B, C)."""

    # STUDENT CODE
    # TODO 3:   Implement this function.
    # NOTE:     The following lines can be removed. They prevent the framework
    #           from crashing.

    res = A * x + B * y + C

    # END STUDENT CODE

    return res


def draw_triangle(framebuffer: Framebuffer, v1: MeshVertex, v2: MeshVertex, v3: MeshVertex):
    """ draws a triangle defined by v1,v2,v3 to the given framebuffer"""

    x1, y1, depth1 = v1.get_screen_coordinates()
    x2, y2, depth2 = v2.get_screen_coordinates()
    x3, y3, depth3 = v3.get_screen_coordinates()

    col1 = v1.get_color()
    col2 = v2.get_color()
    col3 = v3.get_color()

    # calc triangle area * 2
    a = ((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1))

    if not np.isclose(a, 0):
        # Swap order of clockwise triangle to make them counter-clockwise
        if a < 0:
            t = x2
            x2 = x3
            x3 = t

            t = y2
            y2 = y3
            y3 = t

            t = depth2
            depth2 = depth3
            depth3 = t

            t = col2
            col2 = col3
            col3 = t

        # STUDENT CODE
        # TODO 3: Implement this function.
        # HINT:   Don't forget to implement the function lineEq!
        #         Read the instructions and tutorial.py for further explanations!
        # BONUS:  Solve this task without using loops.

        # Determine bounding box
        min_x = min(x1, x2, x3)
        max_x = max(x1, x2, x3)
        min_y = min(y1, y2, y3)
        max_y = max(y1, y2, y3)

        # Berechnung der Kantenvektoren
        e1x = x3-x2
        e1y = y3-y2

        e2x = x1-x3
        e2y = y1-y3

        e3x = x2-x1
        e3y = y2-y1

        A1 = -e1y
        A2 = -e2y
        A3 = -e3y

        B1 = e1x
        B2 = e2x
        B3 = e3x

        C1 = -(A1*x2 + B1*y2)
        C2 = -(A2*x3 + B2*y3)
        C3 = -(A3*x1 + B3*y1)

        # Berechnung der Normalvektoren
        f1 = line_eq(A1, B1, C1, x1, y1)
        f2 = line_eq(A2, B2, C2, x2, y2)
        f3 = line_eq(A3, B3, C3, x3, y3)

        for y in range(int(min_y), int(max_y) + 1):
            for x in range(int(min_x), int(max_x) + 1):
                O1 = line_eq(A1, B1, C1, x, y)
                O2 = line_eq(A2, B2, C2, x, y)
                O3 = line_eq(A3, B3, C3, x, y)

                # innerhalb
                alpha = O1/f1
                beta = O2/f2
                gamma = O3/f3
                if O1 <= 0 and O2 <= 0 and O3 <= 0:
                    color = MeshVertex.barycentric_mix(
                        col1, col2, col3, alpha, beta, gamma)
                    depth = MeshVertex.barycentric_mix(
                        depth1, depth2, depth3, alpha, beta, gamma)
                    framebuffer.set_pixel(
                        [x], [y], depth, color)

        # END STUDENT CODE
