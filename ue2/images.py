import numpy as np
import scipy.ndimage
from PIL import Image

import utils


def read_img(inp: str) -> Image.Image:
    """
        Returns a PIL Image given by its input path.
    """
    img = Image.open(inp)
    return img


def convert(img: Image.Image) -> np.ndarray:
    """
        Converts a PIL image [0,255] to a numpy array [0,1].
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.array(img) / 255

    # END STUDENT CODE
    return out


def switch_channels(img: np.ndarray) -> np.ndarray:
    """
        Swaps the red and green channel of a RGB iamge given by a numpy array.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.zeros(img.shape)
    out = np.copy(img)
    out[:, :, 0] = img[:, :, 1]
    out[:, :, 1] = img[:, :, 0]
    return out


def image_mark_green(img: np.ndarray) -> np.ndarray:
    """
        returns a numpy-array (HxW) with 1 where the green channel of the input image is greater or equal than 0.7, otherwise zero.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    mask = np.zeros((img.shape[0], img.shape[1]))
    # mask ist dann nur noch 2-dimensional
    mask[:, :] = img[:, :, 1]
    mask = mask >= 0.7

    # END STUDENT CODE

    return mask


def image_masked(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
        sets the pixels of the input image to zero where the mask is 1.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.copy(img)

    # in each value where mask is true, the value is set to [0,0,0]
    out[mask] = [0, 0, 0]

    # END STUDENT CODE
    return out


def grayscale(img: np.ndarray) -> np.ndarray:
    """
        Returns a grayscale image of the input. Use utils.rgb2gray().
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = utils.rgb2gray(img)
    # END STUDENT CODE

    return out


def cut_and_reshape(img_gray: np.ndarray) -> np.ndarray:
    """
        Cuts the image in half (x-dim) and stacks it together in y-dim.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.zeros((1024, 256))

    half_image_width = img_gray.shape[1]//2
    left_side = img_gray[:, :half_image_width]
    right_side = img_gray[:, half_image_width:]
    out = np.concatenate((right_side, left_side), axis=0)

    # END STUDENT CODE

    return out


def filter_image(img: np.ndarray) -> np.ndarray:
    """
        filters the image with the gaussian kernel given below.
    """
    gaussian = utils.gauss_filter(5, 2)
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    height, width, channels = img.shape
    kernel_size = gaussian.shape[0]

    # floor division
    padding_size = kernel_size // 2

    # Padding hinzufügen, um die Kanten des Bildes zu behandeln
    padded_img = np.zeros(
        (height + 2 * padding_size, width + 2 * padding_size, channels))

    # Die Parameter von Pad geben jeweils an,
    # um wie viel das Array vergößert werden soll in 1.,2. und 3. dimension
    # mode = constant sagt, dass es mit einem konstanten Wert (hier 0) gefüllt werden soll.
    padded_img = np.pad(img, ((padding_size, padding_size),
                              (padding_size, padding_size), (0, 0)), mode='constant')

    # Ausgabebild initialisieren
    filtered_img = np.zeros_like(img)

    # könnte man auch schreiben als: (convolve ist von scipy.ndimage)
    # for channel in range(img.shape[2]):
    #     filtered_img[:, :, channel] = convolve(padded_img[:, :, channel], gaussian_kernel)

    # Filter über das Bild anwenden
    for i in range(padding_size, height + padding_size):
        filter_height_from = i - padding_size
        filter_height_to = i + padding_size + 1
        for j in range(padding_size, width + padding_size):
            filter_width_from = j - padding_size
            filter_width_to = j + padding_size + 1
            for k in range(channels):
                patch = padded_img[filter_height_from:filter_height_to,
                                   filter_width_from:filter_width_to, k]

                # save the sum of the pixel
                filtered_img[filter_height_from,
                             filter_width_from, k] = np.sum(patch * gaussian)

    return filtered_img


def horizontal_edges(img: np.ndarray) -> np.ndarray:
    """
        Defines a sobel kernel to extract horizontal edges and convolves the image with it.
    """
    # STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    G_horizontal = np.array([[1, 2, 1],
                             [0, 0, 0],
                             [-1, -2, -1]])

    # scipy.ndimage.correlate  berechnet die diskrete Kreuzkorrelation
    # zwischen einem Input-Array und einem Filter-Kernel.
    # Der Filter-Kernel wird über das Input-Array verschoben. Dann wird an jeder Stelle
    # das Skalarprodukt zwischen den Werten im Input-Array und dem Filter-Kernel berechnet.
    filtered_img = scipy.ndimage.correlate(img, G_horizontal, mode='constant')

    # END STUDENT CODE

    return filtered_img
