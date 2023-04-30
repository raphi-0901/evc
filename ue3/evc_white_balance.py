# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np


def evc_white_balance(input_image: np.ndarray, white: np.ndarray) -> np.ndarray:
    """evc_white_balance performs white balancing manually.

      INPUT
      input       ... image
      white       ... a color (as RGB vector) that should become the new white

      OUTPUT
      result      ... result after white balance"""

    # STUDENT CODE
    # TODO: perform white balancing using the 'white' variable
    # HINT: Make sure the program does not crash if 'white' is zero!
    # NOTE: pixels brighter than 'white' will have values > 1.
    #       This requires a normalization which will be performed
    #       during the histogram clipping.
    # NOTE: The following line can be removed. It prevents the framework
    #       from crashing.

    result = np.copy(input_image)
    if np.all(white != 0):
        # result[:, :, 0] = result[:, :, 0] / white[0]
        # result[:, :, 1] = result[:, :, 1] / white[1]
        # result[:, :, 2] = result[:, :, 2] / white[2]
        result = result / white

    # END STUDENT CODE

    result = np.minimum(result, 1)
    return result
