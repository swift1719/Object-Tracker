import cv2

i1 = cv2.imread('f:/TE_PBL/resource/1.jpg')  # frame1
i2 = cv2.imread('f:/TE_PBL/resource/2.jpg')  # frame2
i3 = cv2.imread('f:/TE_PBL/resource/3.jpg')  # frame3
i4 = cv2.imread('f:/TE_PBL/resource/4.jpg')  # frame4
i5 = cv2.imread('f:/TE_PBL/resource/5.jpg')  # frame5

d1 = cv2.absdiff(i1, i2)
d2 = cv2.absdiff(i2, i3)
d3 = cv2.absdiff(i3, i4)
d4 = cv2.absdiff(i4, i5)

# movement = cv2.bitwise_or(d1, d2)
# movement = cv2.bitwise_or(movement, d3)
# movement = cv2.bitwise_or(movement, d4)

m1 = cv2.bitwise_and(d1, d2)
m2 = cv2.bitwise_and(d2, d3)
m3 = cv2.bitwise_and(d3, d4)

cv2.imwrite('f:/TE_PBL/resource/6.jpg', d1)
cv2.imwrite('f:/TE_PBL/resource/7.jpg', d2)
cv2.imwrite('f:/TE_PBL/resource/8.jpg', d3)
cv2.imwrite('f:/TE_PBL/resource/9.jpg', d4)

cv2.imwrite('f:/TE_PBL/resource/10.jpg', m1)
cv2.imwrite('f:/TE_PBL/resource/11.jpg', m2)
cv2.imwrite('f:/TE_PBL/resource/12.jpg', m3)
