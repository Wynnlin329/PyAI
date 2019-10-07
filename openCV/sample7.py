import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyimage= image.copy()#mask要比原要抓的圖上下左右個多1，所以要多2(表示處理區域)
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    (b,g,r) = copyimage[455,250]#455從圖片左上開始算
    print('位置(250,455)處的像素 -紅:%d,綠:%d,藍:%d'%(r,g,b))
    cv.floodFill(copyimage,mask,(250,455),(0,255,255),(30,30,30),(40,40,40),cv.FLOODFILL_FIXED_RANGE)#對哪填充 ,對哪運算 ,種子點,要填充的顏色,範圍最低,最高點
    cv.imshow('fill_color_demo',copyimage)


def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:]=255#100~300範圍白色，:三個通道255

    mask = np.ones([400 + 2, 400 + 2], np.uint8)
    mask[99:301,99:301]=0#mask必須要0,mask_only才可作用
    cv.floodFill(image, mask, (250, 200), (0, 0, 255),cv.FLOODFILL_MASK_ONLY)  # mask_only只針對0的部分做
    cv.imshow('fill_binary',image)



print('------hello python-----')
src = cv.imread('E:\PYAI\image\image1.jpg')
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
fill_color_demo(src)

fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()