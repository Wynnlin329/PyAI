import cv2 as cv
import numpy as np



def threshold_demo(image):    #全域值
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)     # THRESH_OTSU 自適應值
    #ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    #ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)
    print("threshold value %s"%ret)
    cv.imshow("binary",binary)

def local_threshold(image):   #區域值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25, 10)
    cv.imshow("binary",binary)


print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI\image/binaryImageTest.jpg")              # 讀取圖檔
cv.imshow("Input Image",src)                        # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)

threshold_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")