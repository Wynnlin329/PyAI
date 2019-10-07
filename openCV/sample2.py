import cv2 as cv
import numpy as np

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow('gray',gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('yuv', yuv)
    YCbCr = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('YCbCr',YCbCr)

print('------hello python-----')
src = cv.imread('E:\PYAI\image\TargetImage.jpg')
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
color_space_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()