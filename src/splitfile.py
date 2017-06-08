# from subprocess import call

import os
import subprocess


def splitVideoIntoFrames(filename):

    if not os.path.isfile(filename):
        return

    tmpDir = os.path.dirname(filename) + "/tmp"
    if not os.path.exists(tmpDir):
        os.makedirs(tmpDir)

    print("splitting file into frames: " + filename)
    subprocess.call(["ffmpeg", "-i", filename, "" + tmpDir + "/%d.bmp"] )

    return

splitVideoIntoFrames("/home/gukoessler/PycharmProjects/sintel_trailer/av1_sintel_480p/1000_480_sintel.raw")