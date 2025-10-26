import cv2 as cv
import numpy as np

empty = np.zeros((600,600,3),dtype='uint8')

cv.imshow('Empty',empty)

empty[200:300,300:400]= 0,0,255  # [:] means All Pixels   ,   color in Open CV : BGR  - not RGB

cv.imshow('Color',empty)

# Draw Rectangle

cv.rectangle(empty,(0,0),((empty.shape[1]//2),(empty.shape[1]//2)),(0,255,255),thickness=-3)
cv.imshow('Rectangle',empty)

# Draw Line

cv.line(empty,(0,0),((empty.shape[1]//2),(empty.shape[1]//2)),(255,255,255),3)
cv.imshow('Line',empty)

# Draw Circle

cv.circle(empty,(500,500),50,(255,255,255),3)
cv.imshow('Circle',empty)

# Write a Text
cv.putText(empty,"Hi , This is a text",(150,400),cv.FONT_HERSHEY_DUPLEX,1.0,(0,0,255),thickness=2)
cv.imshow('Text',empty)

cv.waitKey(0)
cv.destroyAllWindows()