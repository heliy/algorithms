# coding: UTF-8

"""
Input and output of image file.

------------
img2array(): Read image file as numpy array

"""

__all__ = ["img2array"]


import matplotlib.image as img
from imgContents import *

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.299, 0.587, 0.144])

def isRGB(image):
    shape = list(image.shape)
    return len(shape) == 3 and shape[-1] == 3

def isGray(image):
    return len(image.shape) == 2

def img2array(fname, mode=RGB):
    """
    Read image file as numpy array.
    -----------
    Input:
      fname: input file name.
      mode: image mode;
         "RGB": RGB mode, return as M*N*3 matrix, defualt;
         "Gray": Grayscale, return as M*N matrix.
    output:
      array: numpy array, shape depends upon `mode`.
    """
    image = img.imread(fname)
    if mode == RGB:
        if is not isRGB(image):
            raise image+" is not a RGB image file!"
        else:
            return image
    elif mode == Grayscale:
        if isGray(image):
            return image
        elif isRGB(image):
            return rgb2gray(image)
        else:
            raise image+"is not a RGB or Grayscale image file."
    else:
        raise "Unknown image input mode: "+mode+"!"
