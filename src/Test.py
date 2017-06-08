import os, sys
import math
import numpy
# import PSNR
import scipy.misc


def psnr(image1, image2):
    mse = numpy.mean((image1 - image2) ** 2)
    if mse == 0:
        return 100
    max_value = 255.0
    return 20 * math.log10(max_value / math.sqrt(mse))


image_ref1 = 'image1.jpg'
image_ref2 = 'image2.jpg'


image1 = scipy.misc.imread(image_ref1, flatten=True).astype(numpy.float32)
image2 = scipy.misc.imread(image_ref2, flatten=True).astype(numpy.float32)

psnr_value = psnr(image1, image1)

print(psnr_value)

