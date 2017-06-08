import sys
import os
import numpy
import scipy.misc
import PSNR
import FileSplitter
import PSNResults
import pickle

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

if len(sys.argv) != 3:
    print("must have 2 arguments: #" + str(len(sys.argv) - 1))
    sys.exit()

args = sys.argv
input_folder = args[1]
output_folder = args[2]
working_directory = os.path.dirname(os.path.abspath(__file__))
bitrates = []

#Ordner fuer die Videos
videoFolders = listdir_nohidden(os.path.join(working_directory, input_folder))

outputPath = os.path.join(working_directory, output_folder)

#OutputFolder erzeugen
if not os.path.exists(outputPath):
    os.makedirs(outputPath)

#Metriken fuer alle Videos berechnen
for videoFolder in videoFolders:
    if not videoFolder.startswith("."):
        videoFolderPath = os.path.join(working_directory, input_folder, videoFolder)

        # Subfolder in Outputfolder erstellen
        videoOutputPath = os.path.join(outputPath, videoFolder)

        if not os.path.exists(videoOutputPath):
            os.makedirs(videoOutputPath)


        #Pfade fuer die src Dateien
        rawPath = os.path.join(videoFolderPath, "raw")
        av1Path = os.path.join(videoFolderPath, "av1")
        h265Path = os.path.join(videoFolderPath, "h265")

        #Unkomprimiertes Video in PNG Frames splitten
        rawFile = os.path.join(rawPath, listdir_nohidden(rawPath)[0])
        FileSplitter.splitVideoIntoFrames(rawFile)

        bitrates = []
        psnrs = []

        AV1files = listdir_nohidden(av1Path)
        RAWFiles = listdir_nohidden(os.path.join(rawPath, "tmp"))
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
            AV1Tmpfiles = listdir_nohidden(os.path.join(av1Path, "tmp"))
            AV1Tmpfiles.sort()

            for i in range(1, len(RAWFiles)):
                imageRaw = scipy.misc.imread(os.path.join(rawPath, "tmp", RAWFiles[i]), flatten=True).astype(numpy.float32)
                imageEnc = scipy.misc.imread(os.path.join(av1Path, "tmp", AV1Tmpfiles[i]), flatten=True).astype(numpy.float32)
                psnrs.append(PSNR.psnr(imageRaw, imageEnc))

            meanpsnr = numpy.mean(psnrs)
            result = PSNResults(meanpsnr, bitrate)

            #Output File erzeugen bzw. erweitern
            if os.path.isfile(os.path.join(videoOutputPath, "psnr")):
                print("lade dieses File")
            else:
                pickle.dump(result)

            print("AV1 mean psnr: " + str(meanpsnr) + "Bitrate: " + str(bitrate) + "Folder" + av1Path)


print("test")
#image1 = scipy.misc.imread(image_ref1, flatten=True).astype(numpy.float32)
#image2 = scipy.misc.imread(image_ref2, flatten=True).astype(numpy.float32)




