import cv2 as cv
import numpy as np

def pyramid_demo(image):      #高斯金字塔
    level = 3
    temp = image.copy()
    pyramid_image = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_image.append(dst)
        cv.imshow('pyramid_demo'+str(i),dst)
        temp = dst.copy()
    return pyramid_image












print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI\image/lena_color.jpg")                   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
#Laplacian_demo(src)

pyramid_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗
