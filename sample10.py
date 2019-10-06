import cv2 as cv
import numpy as np

def bi_image(image):#邊緣保留濾波
    dst = cv.bilateralFilter(image,0,100,15)#1原影像,2半徑(預設0),3顏色資訊(越大越糊ex100),4空間資訊(ex15)
    #dst1 = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_image",dst)
    #cv.imshow("bi_image1", dst1)

def mean_shift_demo(image):   # 定義均值偏移濾波
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)#1,2空間差異值,3色彩差異值
    cv.imshow("mean_shift_demo", dst)



print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI\image/bi_testImage.png")               # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)                         # 顯示圖片

mean_shift_demo(src)
bi_image(src)


cv.waitKey(0)                                        # 等待使用者按按鍵
cv.destroyWindow("Input Image")                      # 關閉視窗

