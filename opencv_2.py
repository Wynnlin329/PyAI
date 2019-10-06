import cv2 as cv
import numpy as np

def access_pixels(image): #讀影像資訊
    print(image.shape)
    height=image.shape[0]
    width=image.shape[1]
    channel= image.shape[2]
    print('height: %s,width: %s, channel: %s'%(height,width,channel))
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row,col,c]
                image[row, col, c] = 255- pv#修改像素
    cv.imshow('access_pixels',image)

def inverse(image):
    dst = cv.bitwise_not(image)#遮罩255-位元=not
    cv.imshow("inverse",dst)


#====創造圖片=============
def create_image():


    m1=np.ones([3,3],np.float32)#把3*3矩陣數值改變
    m1.fill(369)
    print(m1)

    m2=m1.reshape([1,9])#改為1*9矩陣
    print(m2)

    # img = np.zeros([400,400,3],np.uint8)#創一個陣列
    # img[:,:,0]= np.ones([400,400])*255#第0通道(B通道)
    # cv.imshow('create_image',img)

    # img = np.ones([400,400,1],np.uint8)
    # img = img*100
    # cv.imshow('create_image',img)
#====================




#顯示圖片-----------------------
# def video_demo():
#     capture = cv.VideoCapture(0)#0表示編號0的webcam或路徑
#     while(True):
#         ret,frame = capture.read()#(read會回傳兩個參數，一個讀完了沒 一個讀的地方)讀進來的影片放Frame,ret來判斷是否已到盡頭
#         frame = cv.flip(frame,1)#1水平反轉,0上下顛倒,-1都有
#         cv.imshow('video',frame)
#         c=cv.waitKey(50)#50毫秒讀鍵盤一次
#         if c==27:   #27=esc鍵
#             break
#--------------------------------
#顯示圖像資訊
# def git_image_info(image):
#     print(type(image))
#     print(image.shape)
#     print(image.size)
#     print(image.dtype)
#     np.array(image)#numpy底下的array
#     pixel_data = np.array(image)
#     print(pixel_data)
#-----------


print('------hello python-----')
src = cv.imread('E:\PYAI\image\TargetImage.jpg')
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
create_image()
inverse(src)
# git_image_info(src)
# gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)#cvtcolor色彩空間轉換，轉灰階
# cv.imwrite('E:/gray001.jpg',gray)
#抓時間
# t1 = cv.getTickCount()#讀出第一個clock
access_pixels(src)
# t2 = cv.getTickCount()#s讀出第二個clock
# time = (t2-t1)/cv.getTickFrequency() #1000 *總次數/一秒內重複的次數= 時間(ms)
# print("Time : %s"%(time*1000))#顯示毫秒

cv.waitKey(0)
cv.destroyAllWindows()