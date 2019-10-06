import cv2 as cv
import numpy as np



# def extrace_hair(image):
#     hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
#     cv.imshow('hsv',hsv)
#     low_hsv = np.array([0,0,0])
#     high_hsv= np.array([180,255,46])#黑色閥值
#     dst = cv.inRange(hsv,low_hsv,high_hsv)#取出最低值與最高值的範圍
#     cv.imshow('result',dst)

def exreace_object_demo():
     capture = cv.VideoCapture(0)#0表示編號0的webcam或路徑
     while(True):
         ret,frame = capture.read()#(read會回傳兩個參數，一個讀完了沒 一個讀的地方)讀進來的影片放Frame,ret來判斷是否已到盡頭
         frame = cv.flip(frame,1)#1水平反轉,0上下顛倒,-1都有
         hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
         cv.imshow('hsv', hsv)
         low_hsv = np.array([35, 43, 46])
         high_hsv = np.array([77, 255, 255])  # 黑色閥值
         dst = cv.inRange(hsv, low_hsv, high_hsv)
         cv.imshow('mask',dst)
         cv.imshow('Video',frame)
         c=cv.waitKey(50)#50毫秒讀鍵盤一次
         if c==27:   #27=esc鍵
             break


print('------hello python-----')
src = cv.imread('E:\PYAI\image\TargetImage.jpg')
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
exreace_object_demo()
# b,g,r = cv.split(src)#抓出三種像素
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
# src1 =cv.merge([b,g,r])
# cv.imshow('src1 image',src1)
cv.waitKey(0)
cv.destroyAllWindows()

