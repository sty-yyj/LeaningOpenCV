import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('LearnOpenCV/img/messi6.jpg')


def nothing(x):
    pass

cv.namedWindow('image')

cv.createTrackbar('Threshold1', 'image', 0, 127, nothing)
cv.createTrackbar('Threshold2', 'image', 0, 255, nothing)

while(1):

    Threshold1 = cv.getTrackbarPos('Threshold1', 'image')
    Threshold2 = cv.getTrackbarPos('Threshold2', 'image')

    edges = cv.Canny(img, Threshold1, Threshold2)

    cv.imshow('image', edges)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()