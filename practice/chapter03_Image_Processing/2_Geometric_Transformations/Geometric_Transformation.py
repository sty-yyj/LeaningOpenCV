import numpy as np
import cv2 as cv

# # Scaling
# img = cv.imread('LearnOpenCV/img/messi6.jpg')
# height, width = img.shape[:2]
# res = cv.resize(img, (2*width, 2*height), interpolation = cv.INTER_CUBIC)
# cv.imshow('image', res)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # Translation
# img = cv.imread('LearnOpenCV/img/messi6.jpg', 0)
# rows, cols = img.shape

# M = np.float32([[1, 0, 100], [0, 1, 50]])
# dst = cv.warpAffine(img, M, (cols, rows))
# cv.imshow('image', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Rotation
img = cv.imread('LearnOpenCV/img/messi6.jpg', 0)
rows, cols = img.shape

M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('image', dst)
cv.waitKey(0)
cv.destroyAllWindows()