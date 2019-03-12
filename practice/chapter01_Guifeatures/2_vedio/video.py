import numpy as np
import cv2 as cv

###########################################################
# Capture Video from Camera
###########################################################
# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print('Cannot open camera')
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame(stream end?). Exiting")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame', gray)
#     if cv.waitKey(1)  == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

###########################################################
# Playing Video from file
###########################################################
# cap = cv.VideoCapture('LearnOpenCV/img/vtest.avi')

# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()

###########################################################
# Saving a Video
###########################################################
cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # frame = cv.flip(frame, 0)
    # write the flipped frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(gray)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()