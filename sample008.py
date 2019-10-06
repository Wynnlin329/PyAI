import cv2 as cv
import numpy as np


def blur_demo(image):#均值模糊
    det = cv.blur(image,(5,5))#mask要模糊化的大小
    cv.imshow("blur",det)


def median_blur_demo(image):#中值模糊
    det = cv.medianBlur(image,5)#必須要是奇數5*5
    cv.imshow("medan_blur_demo", det)


def custon_blur_demo(image): #銳化                                                 #自訂義卷積
    #kernel = np.ones([5,5],np.float32)/25                                    #自訂義的 filter  一維
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0,-1, 0]], np.float32)       # 自訂義的 filter 二維 (銳化)
    det = cv.filter2D(image,-1,kernel = kernel)#-1:跟原來影像深度 channel數是一樣的
    cv.imshow("custon_blur_demo", det)


print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI\image/image1.jpg")               # 讀取圖檔(均值模糊，銳化)
#src = cv.imread("E:/Image/Lenanoise.jpg")           # 讀取圖檔(中值模糊)
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)                         # 顯示圖片
#blur_demo(src)
#median_blur_demo(src)
custon_blur_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗

