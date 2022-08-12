import numpy as np
import cv2

# 设置颜色阈值
# 其中，lower为阈值下限，higher为阈值上限
font = cv2.FONT_HERSHEY_SIMPLEX

'''
可以自己添加或者修改颜色，调整图像的BGR参数即可
'''

# 红色阈值
lower_red = np.array([0, 140, 180])
higher_red = np.array([8, 255, 255])
# 绿色阈值
lower_green = np.array([65, 120, 76])
higher_green = np.array([85, 255, 255])
# 黄色阈值
lower_yellow = np.array([25, 70, 70])
higher_yellow = np.array([35, 255, 255])

# 提取颜色面积最小值
[x_min , y_min] = [0,0]

# 调用摄像头
cap = cv2.VideoCapture(0)  # 打开电脑内置摄像头

while True:
    ret, frame = cap.read()  # 按帧读取
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 对四种颜色进行滤波
    mask_red = cv2.inRange(img_hsv, lower_red, higher_red)  # 获得掩膜,去掉背景
    mask_red = cv2.medianBlur(mask_red, 7)  # 中值滤波
    mask_green = cv2.inRange(img_hsv, lower_green, higher_green) 
    mask_green = cv2.medianBlur(mask_green, 7)  # 
    mask_yellow = cv2.inRange(img_hsv, lower_yellow, higher_yellow) 
    mask_yellow = cv2.medianBlur(mask_yellow, 7)  # 

    # mask = cv2.bitwise_or(mask_red, mask_red)  # 三部分掩膜进行按位或运算

    cnts1,__ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 轮廓检测
    cnts2,__ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts3,__ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 返回选定颜色矩阵
    for cnt in cnts1:
        (x, y, w, h) = cv2.boundingRect(cnt)  # 返回矩阵坐标
        cv2.rectangle(frame, (x - x_min, y - y_min), (x + w, y + h), (0, 0, 255), 2)  # 框取颜色
        cv2.putText(frame, 'red', (x - x_min, y), font, 0.7, (0, 0, 255), 2)
    for cnt in cnts2:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x - x_min, y - y_min), (x + w, y + h), (30, 255, 255), 2)  # 将检测到的颜色框起来
        cv2.putText(frame, 'yellow', (x - x_min, y - y_min), font, 0.7, (30, 255, 255), 2)
    for cnt in cnts3:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x - x_min, y - y_min), (x + w, y + h), (0, 255, 0), 2)  # 将检测到的颜色框起来
        cv2.putText(frame, 'green', (x -x_min, y - y_min), font, 0.7, (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(10) & 0xFF

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()