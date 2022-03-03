import numpy as np
from skimage import color


def rgb2lab(rgb):
    rgb_ = np.moveaxis(rgb, 0, 2)
    hsl = color.rgb2lab(rgb=rgb_)
    return np.moveaxis(hsl, 2, 0)


def lab2rgb(lab):
    lab_ = np.moveaxis(lab, 0, 2)
    rgb = color.lab2rgb(lab=lab_)
    return np.moveaxis(rgb, 2, 0)
