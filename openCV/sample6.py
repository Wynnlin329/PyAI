import cv2 as cv
import numpy as np


print('------hello python-----')
src = cv.imread('E:\PYAI\image\image2.jpg')
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)

face = src[80:270,180:330]
#cv.imshow('face image',face)
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)#灰階1個通道
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)#轉三通道
src[80:270,180:330]=backface
cv.imshow('face',src)


cv.imshow('gray',gray)



cv.waitKey(0)
cv.destroyAllWindows()