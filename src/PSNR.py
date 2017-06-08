import math
import numpy
import scipy.misc

def psnr(image1, image2):
    mse = numpy.mean((image1 - image2) ** 2)
    if mse == 0:
        return 100
    max_value = 255.0
    return 20 * math.log10(max_value / math.sqrt(mse))


def mean_psnr_for_video(video_name_1, bitrate):
    print("Hello")



