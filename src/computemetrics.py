import sys
import os
import numpy
import scipy.misc
import pickle
import shutil
import pylab
import PSNR
import FileSplitter

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
        for f in listdir_nohidden(rawPath):
            tmp = os.path.join(rawPath,f)
            if os.path.isfile(tmp):
                rawFile = tmp
                break
        FileSplitter.splitVideoIntoFrames(rawFile)

        bitrates = []
        psnrs = []

        AV1files = sorted(listdir_nohidden(av1Path))
        H265files = sorted(listdir_nohidden(h265Path))
        RAWFiles = sorted(listdir_nohidden(os.path.join(rawPath, "tmp")))
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
            AV1Tmpfiles = sorted(listdir_nohidden(os.path.join(av1Path, "tmp")))

            print("computing psnrs for each frame")
            for i in range(1, len(RAWFiles)):
                imageRaw = scipy.misc.imread(os.path.join(rawPath, "tmp", RAWFiles[i]), flatten=True).astype(numpy.float32)
                imageEnc = scipy.misc.imread(os.path.join(av1Path, "tmp", AV1Tmpfiles[i]), flatten=True).astype(numpy.float32)
                psnrs.append(PSNR.psnr(imageRaw, imageEnc))

            meanpsnr = numpy.mean(psnrs)
            # result = PSNResults(meanpsnr, bitrate)
            result = [{"bitrate" : bitrate,"meanpsnr" : meanpsnr}]

            #Output File erzeugen bzw. erweitern
            outFile = os.path.join(videoOutputPath, "av1_psnr.pickle")
            if not os.path.isfile(outFile):
                with open(outFile, 'wb') as f:
                    pickle.dump(result, f, pickle.HIGHEST_PROTOCOL)
            else:
                with open(outFile, 'rb') as f:
                    tmpresult = pickle.load(f)
                    tmpresult.append(result[0])
                with open(outFile, 'wb') as f:
                    pickle.dump(tmpresult, f, pickle.HIGHEST_PROTOCOL)

            print("AV1 mean psnr: " + str(meanpsnr) + " - Bitrate: " + str(bitrate) + " - Folder" + av1Path)
            shutil.rmtree(os.path.join(av1Path, "tmp"))

            ####################################################################
            for h265file in H265files:
                if h265file.startswith(str(bitrate)):
                    FileSplitter.splitVideoIntoFrames(os.path.join(h265Path,h265file))
                    break
            # compute psnr && remove tmp folder for av1
            H265Tmpfiles = sorted(listdir_nohidden(os.path.join(h265Path, "tmp")))

            print("computing psnrs for each frame")
            for i in range(1, len(RAWFiles)):
                imageRaw = scipy.misc.imread(os.path.join(rawPath, "tmp", RAWFiles[i]), flatten=True).astype(numpy.float32)
                imageEnc = scipy.misc.imread(os.path.join(h265Path, "tmp", H265Tmpfiles[i]), flatten=True).astype(numpy.float32)
                psnrs.append(PSNR.psnr(imageRaw, imageEnc))

            meanpsnr = numpy.mean(psnrs)
            # result = PSNResults(meanpsnr, bitrate)
            result = [{"bitrate" : bitrate,"meanpsnr" : meanpsnr}]

            #Output File erzeugen bzw. erweitern
            outFile = os.path.join(videoOutputPath, "h265_psnr.pickle")
            if not os.path.isfile(outFile):
                with open(outFile, 'wb') as f:
                    pickle.dump(result, f, pickle.HIGHEST_PROTOCOL)
            else:
                with open(outFile, 'rb') as f:
                    tmpresult = pickle.load(f)
                    tmpresult.append(result)
                with open(outFile, 'wb') as f:
                    pickle.dump(tmpresult, f, pickle.HIGHEST_PROTOCOL)

            print("H265 mean psnr: " + str(meanpsnr) + " - Bitrate: " + str(bitrate) + " - Folder" + h265Path)
            shutil.rmtree(os.path.join(h265Path, "tmp"))

print("Finished")

