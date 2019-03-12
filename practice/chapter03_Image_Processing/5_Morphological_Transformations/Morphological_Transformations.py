import cv2 as cv
import numpy as np

# Erosion
img = cv.imread('LearnOpenCV/img/j.png')
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)

dilation = cv.dilate(img, kernel, iterations=1)

# Opening is just another name of erosion followed by dilation
# It is useful in removing noise
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

# Closing is reverse of Opening, Dilation followed by Erosion. 
# It is useful in closing small holes inside the foreground objects, or small black points on the object.
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

cv.imshow('image', gradient)
cv.waitKey(0)
cv.destroyAllWindows()