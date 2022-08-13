import cv2
import numpy as np
import time
import os

'''
使用说明：
检索当前路径下是否有path指向的文件夹
如果没有就创建文件夹
会先后录下1、2、3、4、5五种手势的数据（可以自己选择添加或者换成其他的）
需要修改可以调整j变量
'''

# Creaing folder for data
path='./train_location'
if not os.path.exists(path):
    r=input('当前目录下找不到文件夹，是否创建？(T/F)')
    if str(r)=='t' or str(r)=='T':
        os.mkdir(path)
    if str(r)=='f' or str(r)=='F':
        os._exit(0)

# Open Camera object
cap = cv2.VideoCapture(0)

# Decrease frame size
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
j=[0,1,2,3,4]         #Picture Number.
video=False
count=0
ges=0
photo_num=int(input('请输入录制的每种图片数量：'))
time.sleep(1)
print('按l键开始录制')
while True:
    ret, frame = cap.read()
    blur = cv2.GaussianBlur(frame, (3,3), 0)    
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    mask2 = cv2.inRange(hsv,np.array([2,50,50]),np.array([15,255,255]))
    #cv2.imshow('Masked',mask2)

    kernel_square = np.ones((11,11),np.uint8)
    kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    med=cv2.medianBlur(mask2,5)
    cv2.imshow('main',frame)

    cv2.imshow('res',med)
    tex=(200,200) # 选择resize大小
    res_size=cv2.resize(med,tex)
    # cv2.imshow('res',res_size)
    
    if video is True and count < photo_num:
        # 录制训练集
        cv2.imwrite(os.path.join(path,"gest"+str(j[ges])+"_"+str(count)+".jpg"),res_size)
        time.sleep(0.1)
        count += 1
        print("Gesture%d_%d" %(j[ges],count))

    elif video is True and count == photo_num:
        print('{}张测试集手势录制完毕'.format(photo_num))
        video = False
        ges += 1
        if ges < len(j):
            print('此手势录制完成，按l按键录制下一个手势')
            count=0
        else:
            print('手势录制结束，按q退出程序')


    k = cv2.waitKey(10)
    if k == ord('q'):
        break

    elif k == ord('l'):  # 录制手势
        print("Received!!")
        print("录制将在三秒后开始")
        time.sleep(3)
        video = True
        count = 0

cap.release()
cv2.destroyAllWindows()