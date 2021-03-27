#  Histogram Back projection
# Histogram Back projection is a technique that is used for image segmentation
# or finding objects of interest in an image.
# It creates an image of the same size (but single channel) as that of the
# input image, where each pixel corresponds to the probability of that pixel
# belonging to our object.
# The output image will have the object of interest in more white compared to remaining part.


# Spatial Filtering
# Spatial Filtering is an image enhancement method that transforms the intensity
# of a pixel according to the intensities of the neighboring pixels.

# The spatial filter is a matrix mostly of 3×3, 5×5 or 7×7 size.
# The values in the filter are called coefficients or weights.
# The other term to spatial filter is kernel.

# The spatial filtering can be thought of as a shift and multiply operation in
# which the the filter is placed over a portion of an image.
# Then multiplication of the filter weights (or coefficients) and  the
# corresponding image pixel values is done.
# The products are summed up. The center image pixel value is then replaced with
# the result.
# To continue the process the filter is shifted to a new location.

import cv2
import numpy as np

# load the image
img = cv2.imread('F://TE_PBL//histogram backprojection//kids.jpg')
# switch the color space from BGR to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# load the roi
roi = cv2.imread('F://TE_PBL//histogram backprojection//roi.jpg')
# switch the color space from BGR to HSV
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# 2D (hue:channel 0 range 0-179; saturation: channel 1 range 0-255 ) histogram of roi
hist_roi = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Create a mask (histrogram backprojection)
mask = cv2.calcBackProject(images=[hsv_img], channels=[0, 1], hist=hist_roi, ranges=[0, 180, 0, 256], scale=1)

# The mask (back projection, in this case) requires image enhancement.
# For this we would apply spatial filtering using a low pass filter (kernel)
# Expect Convolution : Transformation of intensity of pixels according to the intensities
# of neighbouring pixels.
kernel = np.ones(shape=(7, 7), dtype=np.uint8)
mask = cv2.filter2D(mask, -1, kernel)

# convert the mask from single channel to 3 channel
mask = cv2.merge((mask, mask, mask))

# apply the 3 channel mask on the original image
resultant_img = cv2.bitwise_and(img, mask)

# render
cv2.namedWindow('Original Image', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('ROI', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('Mask', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('Resultant Image', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)

cv2.imshow('Original Image', img)
cv2.imshow('ROI', roi)
cv2.imshow('Mask', mask)
cv2.imshow('Resultant Image', resultant_img)

# wait for press any key
cv2.waitKey(0)
