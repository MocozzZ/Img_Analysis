import cv2
import numpy as np

def getpos(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        #cv2.putText(HSV,str(HSV[y,x]),(200,200),fontFace=5,color=3,fontScale=5)
        print(HSV[y,x])

cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    cv2.imshow("image_HSV",HSV)
    cv2.imshow('image',frame)
    cv2.setMouseCallback("image_HSV",getpos)
    
    k = cv2.waitKey(10) & 0xFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

