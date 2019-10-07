import cv2 as cv
import numpy as np


def create_bgr_hist(image):
    h,w,c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)#只看最高的四個位元，原本8位元，原因為一張圖2的24次芳太大
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b= image[row,col,0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 +np.int(g/bsize)*16+np.int(r/bsize)
            rgbHist[np.int(index),0]=rgbHist[np.int(index),0]+1   #0是哪個通道
    return rgbHist

def hist_comp(image1,image2):
    hist1 = create_bgr_hist(image1)
    hist2 = create_bgr_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)  # 巴氏距離比較，越小越相似
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)  # 相關性比較（最大為1）：越接近1越相似
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)  # 卡方比較，越小越相似
    print("巴氏：%s   相關性：%s   卡方：%s" % (match1, match2, match3))


print("----------- Hello Python ------------")
src1 = cv.imread("E:/PYAI/Image/Image1.jpg")              # 讀取圖檔
src2 = cv.imread("E:/PYAI/Image/Image2.jpg")              # 讀取圖檔
cv.imshow("Input Image",src1)                        # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
#hist_comp(src1,src2)
# 這裡可以讀兩張一樣的圖比較
create_bgr_hist(src2)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗

