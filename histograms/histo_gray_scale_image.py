import random
import cv2
import numpy as np
from matplotlib import pyplot as plt
#Histograms
#A histogram is a representation of distribution of values of a dataset.

#create a 2D array of 300x300, datatype unsigned int (8 bit), each element filled with val 0
#outcome : Single channel gray scale image of size 300x300
img = np.zeros((300,300), dtype=np.uint8)
cv2.rectangle(img, pt1=(100,0), pt2=(199,299), color=127, thickness=-1)
cv2.rectangle(img, pt1=(200,0), pt2=(299,299), color=255, thickness=-1)

print(img)
cv2.imshow('WIN', img)
#make a histogram having 256 bins (intervals) representing values in range 0-255
#img.ravel() to flatten the 2D array to 1D array
plt.hist(img.ravel(), 256, [0,255])
#render the histogram
plt.show()

