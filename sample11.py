import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])#轉一維振烈,bit數,顯示的範圍(ex0-255)
    plt.show('直方圖')

def image_hist(image):
    color = ('blue','green','red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])      # 1原圖,2通道,3沒有指定範圍,4算直方圖每個 bin 的數值
        plt.plot(hist,color = color)                            # 劃書分布圖
        plt.xlim([0,256])                                       # 设置x坐標軸範圍
    plt.show()



print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI\image/image1.jpg")               # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)                         # 顯示圖片
image_hist(src)
#plot_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗
