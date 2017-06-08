import math
import numpy


class PSNR:
    def __init__(self):
        pass

    def psnr(self, image1, image2):
        mse = numpy.mean((image1 - image2) ** 2)
        if mse == 0:
            return 100
        max_value = 255.0
        return 20 * math.log10(max_value / math.sqrt(mse))
