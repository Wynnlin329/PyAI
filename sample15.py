import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread("E:\PYAI/Image/Target2.png")
    target = cv.imread("E:\PYAI/Image/Sample2.png")
    cv.imshow("template image",tpl)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]#高跟寬
    for md in methods:
        print(md)
        result = cv.matchTemplate(target,tpl,md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th);
        cv.rectangle(target,tl,br,(0,0,255),2)
        #cv.imshow("match-" + np.str(md),target)
        cv.imshow("match-(result)" + np.str(md),result)


print("----------- Hello Python ------------")
src = cv.imread("E:\PYAI/Image/Image1.jpg")              # 讀取圖檔
cv.imshow("Input Image",src)                        # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
template_demo()
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗




