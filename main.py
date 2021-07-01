import os
import numpy
import cv2
import re

vidcap = cv2.VideoCapture('shortclip.mp4')
success, image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success, image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

def format(number):
    string = re.sub("[^0-9]", "", number)
    string = int(string)
    if string <= 200:
        string += 200
    else:
        string -= 200
    string = str(string)
    number_os = 3 - len(string)
    for i in range(number_os):
        string = '0' + string
    return string + '.jpg'

#for file in os.listdir():
    #os.rename(file, format(file))
