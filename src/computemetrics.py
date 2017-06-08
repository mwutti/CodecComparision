import sys
import os
import numpy
import scipy.misc
import PSNR
import FileSplitter

if len(sys.argv) != 3:
    print("must have 2 arguments: #" + str(len(sys.argv) - 1))
    sys.exit()

args = sys.argv
input_folder = args[1]
output_folder = args[2]
working_directory = os.path.dirname(os.path.abspath(__file__))


# FileSplitter.splitVideoIntoFrames();

videoFolders = os.listdir(os.path.join(working_directory, input_folder))

for videoFolder in videoFolders:
    videoFolderPath = os.path.join(working_directory, input_folder, videoFolder)
    rawPath = os.path.join(videoFolderPath, "raw")
    av1Path = os.path.join(videoFolderPath, "av1")
    h265Path = os.path.join(videoFolderPath, "h265")
    print(videoFolder)


#image1 = scipy.misc.imread(image_ref1, flatten=True).astype(numpy.float32)
#image2 = scipy.misc.imread(image_ref2, flatten=True).astype(numpy.float32)




