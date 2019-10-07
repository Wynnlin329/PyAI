import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_profect_demo():
    sample = cv.imread("E:\PYAI/Image/Sample.jpg") #樣本
    target = cv.imread("E:\PYAI/Image/TargetImage.jpg")#對應目標
    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    cv.imshow("Sample image",sample)
    cv.imshow("target",target)

    roiHist = cv.calcHist([roi_hsv],[0,1],None,[18,24],[0,180,0,256])
    cv.normalize(roi_hsv,roi_hsv,0,255,cv.NORM_MINMAX)
    dst=cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)#1:縮放一倍(sample)
    cv.imshow('back_projection_demo',dst)





def hist2d_demo(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv],[0,1], None,[180,256],[0,180,0,256])      #計算 HS 兩通道
    # OpenCV中 H 的取值範圍為0 ~180 (8bit儲存時)
    plt.imshow(hist,interpolation='nearest')                  # 用最接近數值的方式統計
    plt.title("2D Histogram")
    plt.show()



print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI/Image/image1.jpg")             # 讀取圖檔
#cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)                         # 顯示圖片
hist2d_demo(src)

#back_profect_demo()
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗
