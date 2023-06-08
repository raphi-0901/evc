# Copyright TU Wien (2022) - EVC: Task 5
# Institute of Computer Graphics and Algorithms.

import numpy as np
from numpy.matlib import repmat

from Mesh import Mesh
from Framebuffer import Framebuffer
from MeshVertex import MeshVertex


def line_rasterization(mesh: Mesh, framebuffer: Framebuffer):
    """ iterates over all faces of mesh and draws lines between
        their vertices.
        mesh                  ... mesh object to rasterize
        framebuffer           ... framebuffer"""

    for i in range(mesh.faces.shape[0]):
        for j in range(mesh.faces[i][0]):
            i, j = np.array(i).reshape(np.asarray(i).size), np.array(
                j).reshape(np.asarray(j).size)

            v1 = mesh.get_face(i).get_vertex(j)
            v2 = mesh.get_face(i).get_vertex(
                np.remainder(j + 1, mesh.faces[i]))
            drawLine(framebuffer, v1, v2)


def drawLine(framebuffer: Framebuffer, v1: MeshVertex, v2: MeshVertex):
    """ draws a line between v1 and v2 into the framebuffer using the
        DDA algorithm.
        framebuffer           ... framebuffer
        v1                    ... vertex 1
        v2                    ... vertex 2"""

    x1, y1, depth1 = v1.get_screen_coordinates()
    x2, y2, depth2 = v2.get_screen_coordinates()

    # STUDENT CODE
    # TO DO: Implement the DDA algorithms to draw a line from v1 to v2 to the given Framebuffer

    # calculate dx , dy
    dx = x2 - x1
    dy = y2 - y1

    # Put pixel for each step
    if (abs(dx) >= abs(dy)):
        step = abs(dx)
    else:
        step = abs(dy)

    dx = dx / step
    dy = dy / step
    x = x1
    y = y1

    for i in range(int(step)):
        t = (i + 1) / step
        # Interpolate color and depth values between v1 and v2
        interpolated_color = MeshVertex.mix(
            v1.get_color(), v2.get_color(), t)
        interpolated_depth = MeshVertex.mix(depth1, depth2, t)

        framebuffer.set_pixel(x, y, interpolated_depth, interpolated_color)
        x += dx
        y += dy

    # END STUDENT CODE
