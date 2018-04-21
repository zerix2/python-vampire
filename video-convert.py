#!/home/mcdade1/anaconda3/bin/python3

"""
Script to convert all of the video files in a target directory to mp3 files.
"""

# Import necessary libraries
import glob
import os

# Get contents of target folder
sources = glob.glob("/home/mcdade1/Desktop/scotts-stuff/*")

# Set output folder
targets = "/home/mcdade1/Desktop/scott-final/"

#print(targets)

# Get files without file extenstion
for file in sources:
    get1 = file.split('.')
    get2 = get1[0].split('/')
    #print(get2[-1])
    #print(outfile[0])
    os.system(f"ffmpeg -i '{file}' -f mp3 -ab 192000 -vn '{targets}{get2[-1]}.mp3'")
