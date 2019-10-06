import cv2 as cv
import numpy as np



def equalHist_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist_demo',dst)


def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))#對比度2.0,處理方塊多大8*8
    dst = clahe.apply(gray)#閥值存clahe
    cv.imshow('clahe_demo',dst)


print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI/Image/HistTest.jpg")             # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)                         # 顯示圖片
clahe_demo(src)

equalHist_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗
