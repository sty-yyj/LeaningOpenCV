###########################################################
# Using OpenCV
###########################################################
# import numpy as np
# import cv2 as cv

# # Read an image
# img = cv.imread('LearnOpenCV/img/apple.jpg')

# # Display an image
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # Create a window and load image to it later
# cv.namedWindow('image0', cv.WINDOW_NORMAL)
# cv.imshow('image0', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # Sum it up
# img = cv.imread('LearnOpenCV/img/apple.jpg', 0)
# cv.imshow('image', img)
# k = cv.waitKey(0) & 0xFF
# if k == 27:            # wait for ESC key to exit
#     cv.destroyAllWindows()
# elif k == ord('s'):    # wait for 's' key to save and exit
#     cv.imwrite('applegray.png', img)
#     cv.destroyAllWindows()

###########################################################
# Using Matplotlib
###########################################################
# import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('LearnOpenCV/img/apple.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
plt.show()