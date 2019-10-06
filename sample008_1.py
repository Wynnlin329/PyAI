import cv2 as cv
import numpy as np

def blur_demo(image):
    det = cv.blur(image,(5,5))
    cv.imshow('blur_deme',det)

def medan_blur_demo(image):
    det = cv.medianBlur(image,5)
    cv.imshow('blur',det)

def custon_blur_demo(image):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
    det = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow('custon_blur_demo',det)

print('------------------hello Python--------------------')
src = cv.imread("E:/PyAI/Image/Image1.jpg")
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow('Input Image',src)
custon_blur_demo(src)
#blur_demo(src)
#medan_blur_demo(src)
cv.waitKey(0)
#cv.destroyAllWindows('Input Image')