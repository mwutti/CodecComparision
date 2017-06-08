import os, sys
import math
import numpy
from PIL import Image

def main():
    image1 = Image.open("image1.jpg")
    image2 = Image.open("image2.jpg")
    psnr_value = psnr(image1, image2)


def psnr(image1, image2):
    mse = numpy.mean((image1 - image2) ** 2)
    if mse == 0:
        return 100
    max_value = 255.0
    return 20 * math.log10(max_value / math.sqrt(mse))

main
