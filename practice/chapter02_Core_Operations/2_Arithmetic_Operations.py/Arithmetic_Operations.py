import numpy as np
import cv2 as cv

# Bitwise Operations
img1 = cv.imread('LearnOpenCV/img/messi6.jpg')
img2 = cv.imread('LearnOpenCV/img/opencv_logo.png')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
print(mask[0])
mask_inv = cv.bitwise_not(mask)
print(mask_inv[0])

img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

img2_fg = cv.bitwise_and(img2, img2, mask=mask)

dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('res', img1)
cv.imshow('img1', img1_bg)
cv.imshow('img2', img2_fg)
cv.imshow('gray', img2gray)
cv.waitKey(0)
cv.destroyAllWindows()