import sys
import os
import numpy
import scipy.misc
import PSNR

if len(sys.argv) != 3:
    print("must have 2 arguments: #" + str(len(sys.argv) - 1))
    sys.exit()

args = sys.argv
input_folder = args[1];
output_folder = args[2];

working_directory = os.path.dirname(os.path.abspath(__file__))

image_ref1 = 'image1.jpg'
image_ref2 = 'image2.jpg'

image1 = scipy.misc.imread(image_ref1, flatten=True).astype(numpy.float32)
image2 = scipy.misc.imread(image_ref2, flatten=True).astype(numpy.float32)

print(PSNR.psnr(image1, image2))

