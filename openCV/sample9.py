import cv2 as cv
import numpy as np


def clamp(pv):
    if pv>255:
        return 255
    if pv<0:
        return  0
    else:
        return pv


def gaussian(image):
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            s=np.random.normal(0,20,3) #0中心點(最高點) 20高斯的寬(scale越小越瘦高，越大越矮),3(3通道的S陣列)
            b = image[row,col,0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow('gaussian_noice',image)


print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI\image/image1.jpg")               # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
#dst = cv.GaussianBlur(src,(0,0),15)
cv.imshow("Input Image",src)                         # 顯示圖片

gaussian(src)



cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗


