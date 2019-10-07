import cv2 as cv
import numpy as np

def extrace_hair(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)
    low_hsv = np.array([0,0,0])
    high_hsv= np.array([180,255,46])#黑色閥值
    dst = cv.inRange(hsv,low_hsv,high_hsv)#取出最低值與最高值的範圍
    cv.imshow('result',dst)





print('------hello python-----')
src = cv.imread('E:\PYAI\image\image1.jpg')
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
extrace_hair(src)

cv.waitKey(0)
cv.destroyAllWindows()