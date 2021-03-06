import os
import subprocess

def splitVideoIntoFrames(filename):

    if not os.path.isfile(filename):
        return

    tmpDir = os.path.dirname(filename) + "/tmp"
    if not os.path.exists(tmpDir):
        os.makedirs(tmpDir)
    else:
        return

    print("splitting file into frames: " + filename)
    FNULL = open(os.devnull, 'w')
    subprocess.call(["ffmpeg", "-i", filename, "" + tmpDir + "/%d.bmp"], stderr=FNULL)
    print("done ...")

    return
