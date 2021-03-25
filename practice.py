import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F://TE_PBL//histogram backprojection//kids.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
roi = cv2.imread('F://TE_PBL//histogram backprojection//roi.jpg')
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

hist_roi = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])

mask = cv2.calcBackProject(images=[hsv_img], channels=[0, 1], hist=hist_roi, ranges=[0, 180, 0, 256], scale=1)

kernel = np.ones(shape=(7, 7), dtype=np.uint8)
mask = cv2.filter2D(mask, -1, kernel)

mask = cv2.merge((mask, mask, mask))

resultant_img = cv2.bitwise_and(img, mask)

cv2.namedWindow('Original Image', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('ROI', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('Mask', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('Resultant Img', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)

cv2.imshow('Original Image', img)
cv2.imshow('ROI', roi)
cv2.imshow('Mask', mask)
cv2.imshow('Resultant Img', resultant_img)

cv2.waitKey(0)

# img = np.zeros((300, 300), dtype=np.uint8)
# cv2.rectangle(img, (0, 100), (99, 199), color=127, thickness=-1)
# cv2.rectangle(img, (100, 100), (199, 199), color=255, thickness=-1)
# cv2.rectangle(img, (200,100), (299, 199), color=185, thickness=-1)
# print(img)
#
# cv2.imshow("view", img)
# plt.hist(img.ravel(), 256, [0, 255])
# plt.show()
# img = cv2.imread('F:/TE_PBL/resource/sample_img.jpg')
# img = cv2.resize(img, (300, 300))
# cv2.imshow('image viewer', img)
#
# for i in range(3):
#     histo = cv2.calcHist([img], [i], None, [256], [0, 255])
#     plt.plot(histo)
#
# plt.hist(img.ravel(), 256, [0, 255])
# plt.show()
# practice
