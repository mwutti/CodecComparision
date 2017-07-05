# Installation and Usage

## Requirements
The Project is implemented and tested with **Python 3.6.1**. 

The following packages must be installed:

  * numpy
  * scipy
  * matplotlib
  
Use **pip install <package-name>** to install the required packages.

The script will create **ffmpeg** subprocesses. Make sure that **ffmpeg** is installed and available in your **$PATH**

## Usage
**$ python computemetrics.py <input-folder> <output-folder>**

  * input-folder: Source Video Folder name located at the same directory as computemetrics.py
  * output-folder: Folder name of outputData located at the same directory as computemetrics.py(must not exist)
## Source Videos

Source Videos must be placed in one folder at the same directory as computemetrics.py. You will provide the foldername 
as a parameter to the script. Create a subfolder for each video you want to analyse. 
    
For each video there must be 3 subfolders. One folder for the raw content called **raw**. One folder for 
the av1 content called **av1**. One folder for the h265 content called **h265**. The files in the av1 and h265
folders must be prefixed with the corresponding bitrate so that the script can find the appropriate videos for 
the calculation.

Example folder Structure:
  * mySourceFolder
    * sintel_trailer_480p
      * raw
        * sintel_trailer_480p.y4m
      * av1
        * 1000_sintel_trailer_480p.av1 
        * 2000_sintel_trailer_480p.av1 
        * 3000_sintel_trailer_480p.av1 
      * h265
        * 1000_sintel_trailer_480p.mp4
        * 1000_sintel_trailer_480p.mp4
        * 1000_sintel_trailer_480p.mp4
    * elephants_dream_480p
      * raw
        * elephants_dreao_480p.y4m
      * av1
        * ...
      * h265
        * ...

## Output Data
For every source video folder the script will create an subfolder in **<output-folder>** with the PSNR-Results.

Example output folder structure

* results
    * sintel_trailer_480p
      * av1_psnr.pickle
      * hs65_psnr.pickle
      * mean_psnr.png
    * elephants_dream_480p
      * av1_psnr.pickle
      * hs65_psnr.pickle
      * mean_psnr.png
      
The PSNR values of the av1 and h265 videos are stored in **.pickle** files for further usage. The computed BD-Curves with
 the BDSNR-values are stored stored in **mean_psnr.png**.
 
## Rough Overview

First we check for correct number of parameters and a valid [folder structure](#source-videos)



## The MIT License

Copyright (c) 2017 Michael Wutti, Günther Kössler

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
