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
bitrates = []

# FileSplitter.splitVideoIntoFrames();

videoFolders = os.listdir(os.path.join(working_directory, input_folder))

for videoFolder in videoFolders:
    videoFolderPath = os.path.join(working_directory, input_folder, videoFolder)
    rawPath = os.path.join(videoFolderPath, "raw")
    av1Path = os.path.join(videoFolderPath, "av1")
    h265Path = os.path.join(videoFolderPath, "h265")
    print(videoFolder)

    rawFile = os.path.join(rawPath,os.listdir(rawPath)[0])
    FileSplitter.splitVideoIntoFrames(rawFile)

    bitrates = []
    psnrs = []

    AV1files = os.listdir(av1Path)
    RAWFiles = os.listdir(os.path.join(rawPath, "tmp"))
    RAWFiles.sort()
    for av1File in AV1files:
        bitrate = av1File.split("_")[0]
        if(bitrate.isdigit()):
            bitrates.append(int(bitrate))

    bitrates.sort()

    # split vids
    for bitrate in bitrates:
        for av1File in AV1files:
            if av1File.startswith(str(bitrate)):
                FileSplitter.splitVideoIntoFrames(os.path.join(av1Path,av1File))
                break
        # compute psnr && remove tmp folder for av1
        AV1Tmpfiles = os.listdir(os.path.join(av1Path, "tmp"))
        AV1Tmpfiles.sort()
        for i in range(1, len(RAWFiles)):
            imageRaw = scipy.misc.imread(os.path.join(rawPath, "tmp", RAWFiles[i]), flatten=True).astype(numpy.float32)
            imageEnc = scipy.misc.imread(os.path.join(av1Path, "tmp", AV1Tmpfiles[i]), flatten=True).astype(numpy.float32)
            psnrs[i] = PSNR.psnr(imageRaw, imageEnc)
        meanpsnr = numpy.mean(psnrs)
        print("AV1 mean psnr: " + str(meanpsnr))

print("test")
#image1 = scipy.misc.imread(image_ref1, flatten=True).astype(numpy.float32)
#image2 = scipy.misc.imread(image_ref2, flatten=True).astype(numpy.float32)




