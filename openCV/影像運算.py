import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow('add_demo',dst)

def substract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow('substract_demo',dst)#show 標題

def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow('divide_demo',dst)

def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1,m2)
    cv.imshow('logic_demo',dst)

def constrast_brightness_demo(image,c,b):#image原影像,C對比度 ,b亮度
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)#元影像是甚麼 出來就是甚麼
    dst = cv.addWeighted(image,c,blank,1-c,b)#C*image+(1-c)*blank+b(偏移植 亮)偏移植可不加
    cv.imshow('constrast_brightness_demo', dst)




print('------hello python-----')
src1 = cv.imread('E:\PYAI\image\WindowsLogo.jpg')#read 路徑
src2 = cv.imread('E:\PYAI\image\LinuxLogo.jpg')




cv.namedWindow('input image1',cv.WINDOW_AUTOSIZE)
cv.imshow('input image1',src1)
# cv.namedWindow('input image2',cv.WINDOW_AUTOSIZE)
# cv.imshow('input image2',src2)
#add_demo(src1,src2)
#substract_demo(src1,src2)
#divide_demo(src1,src2)
# logic_demo(src1,src2)
constrast_brightness_demo(src1,1.2,10)

cv.waitKey(0)
cv.destroyAllWindows()