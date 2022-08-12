import cv2
import numpy as np
import time
import os

#设置保存路径
path='./object_location'
if not os.path.exists(path):
    r=input('当前目录下找不到文件夹，是否创建？(T/F)')
    if str(r)=='t' or str(r)=='T':
        os.mkdir(path)
    if str(r)=='f' or str(r)=='F':
        os._exit(0)

#打开摄像头
cap = cv2.VideoCapture(0)

#初始化参数
video=False
count=0;ges=0
print('按l键开始拍照')

while True:
    ret, frame = cap.read() #视频流帧读取
    cv2.imshow('frame',frame) #显示视频界面

    '''
    此处可以写入图像处理函数来捕捉不同的画面
    '''

    k = cv2.waitKey(10)
    if k == ord('q'): #按下q键退出
        break

    elif k == ord('l'): #按下l键采集
        print("Received!!")
        video = True

    if video is True:
        # 采集数据集
        cv2.imwrite(os.path.join(path,"picture"+str(count)+".jpg"),frame)
        time.sleep(0.5)
        count += 1
        print("picture:%d" %(count))
        ges += 1
        video=False

cap.release()
cv2.destroyAllWindows()