import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# # Simple Thresholding
# img = cv.imread('LearnOpenCV/img/gradient.png', 0)
# ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
# ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
# ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

# Adaptive Thresholding
# img = cv.imread('LearnOpenCV/img/sudoku.png')
# img = cv.medianBlur(img, 5)

# ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(
#     img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
# th3 = cv.adaptiveThreshold(
#     img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

# Ostu's Binarization
