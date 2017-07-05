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

First we check for correct number of parameters and a valid [folder/file structure](#source-videos). After that we create in each folder a tmp folder. The tmp folder will hold all frames which are extracted with ffmpeg. We need those frames for calculation purposes. Once we are done with our calculations we save the results to .pickle files and delete those tmp folders except the tmp folder in the raw folder. We repeat this step for every video in the source folder. At the end we remove the last tmp folder in 'raw'. 

Once ever calculation is done and the tmp folders are removed we read the previously created pickle files, calculate the overall Bjontegaard Delta and plot the metric. Due to the smoothing of the curve with Numpys linspace function it may seem like something went during calculation which is not the case (e.g. first two bitrate have same result and the third is higher and thus we have a convex curve between the first two).

## Adding a new Metric

As of now we implemented PSNR and Bjontegaard Delta. If you which to add a new metric calculation you have need to change/add after following lines:

### Change:
1. Line 9 - import your python function
2. Line 92 & 125 - append the intermediate result array 

### Add:
1. Line 9 - import your python function
2. Line 92 & 125 - create another intermediate result array and append it
3. Line 94 & 127 - calc the mean of your intermediate result array
4. Line 96 & 129 - add your results to the result json object or store them in a different pickle file (99ff & 132ff)
5. Line 147ff - depending on your choice in step 4 you need to read additional files or change line 159 & 165

## The MIT License

Copyright (c) 2017 Michael Wutti, Günther Kössler

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
