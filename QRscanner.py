import code

import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap=cv2.VideoCapture(0)

with open('Author_list.text') as f:
    datalist=f.read().splitlines()

while True:
    success,img=cap.read()
    for barcode in decode(img):
        mydata=barcode.data.decode('utf-8')
        if mydata in datalist:
            myOutput="Authorized"
            mycolor=(0,255,0)
        else:
            myOutput="UN-Authorized"
            mycolor=(0,0,255)

        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,mycolor,2)
        pts2=barcode.rect
        cv2.putText(img,myOutput,[pts2[0],pts2[1]],cv2.FONT_HERSHEY_COMPLEX,0.75,mycolor,2)


    cv2.imshow("webcam", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
