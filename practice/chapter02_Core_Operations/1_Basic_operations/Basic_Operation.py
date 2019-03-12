#%%
import numpy as np
import cv2 as cv

# Load a color image
img = cv.imread('LearnOpenCV/img/messi5.jpg')

#%%
px = img[100, 100]
print(px)

#%%
blue = img[100, 100, 0]
print(blue)

#%%
img[100, 100] = [255, 255, 255]
print(img[100, 100])

#%%
# Better pixel accessing and editing method
img.item(10, 10, 2)

#%%
img.itemset((10, 10, 2), 90)
img.item(10, 10, 2)

#%%
# Image ROI
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

#%%
