import cv2
import numpy as np
from matplotlib import pyplot as plt
#Histograms
#A histogram is a representation of distribution of values of a dataset.

#load an image from the disk
img = cv2.imread('F://TE_PBL//resource//sample_img.jpg')
#resize for processing
img = cv2.resize(img, (300,300))

cv2.imshow('WIN', img)
#make a histogram having 256 bins (intervals) representing values in range 0-255
#img.ravel() to flatten the 2D array to 1D array

for i in range(3):
    histo = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histo)

plt.hist(img.ravel(), 256, [0,255])
#render the histogram
plt.show()

