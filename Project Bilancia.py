from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import math
import serial
import time
import sys
import cv2
import matplotlib.pyplot as plt

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
print(devices)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


while 1:
    ret, img = cap.read()
    cv2.resizeWindow('img', 500,500)
    cv2.line(img,(500,250),(0,250),(0,255,0),1)
    cv2.line(img,(250,0),(250,500),(0,255,0),1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,minNeighbors=2)
    #detecting face and making a rect around it 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(50,255,30),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        arr = {y:y+h, x:x+w}
        #print (arr)
        
        '''print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))'''

    # Center of roi (Rectangle)
        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2
        #print ('xx: ',xx)
        #print ('yy',yy)
        int(xx)
        int(yy)
        center = (xx,yy)
        #print("center: ",center)

    cv2.imshow('img',img)
    
    original_left_vol = volume.GetChannelVolumeLevel(0)
    original_right_vol = volume.GetChannelVolumeLevel(1)
    
    currentVolumeLeft = volume.GetChannelVolumeLevel(0)
    currentVolumeRight = volume.GetChannelVolumeLevel(1)

    print('current vol Left: ', currentVolumeLeft)
    print('current vol Right: ', currentVolumeRight)

  

    if xx < 300 and xx > 200 :
        print("center R")
        if original_left_vol != currentVolumeLeft:
            volume.SetChannelVolumeLevel(0,original_left_vol,None)
            volume.SetChannelVolumeLevel(1,original_right_vol,None)
        
    elif xx < 200 and xx > 100:
        print("right 2")
        
        

        
    elif xx < 100 and xx > 0:
        print("right 3")

        volume.SetChannelVolumeLevel(0,currentVolumeLeft + 3.0,None)
        

        
    elif xx > 300 and xx < 400 :
        print("center L ")
        if original_left_vol != currentVolumeLeft:
            volume.SetChannelVolumeLevel(0,original_left_vol,None)
            volume.SetChannelVolumeLevel(1,original_right_vol,None)

        
    elif xx > 400 and xx <450:
        print("left 2")
        
        
        
    elif xx > 450 and xx <600:
        print("left 3")
    
        volume.SetChannelVolumeLevel(1,currentVolumeRight + 3.0,None)

        
    else:
        print("not recognised pos")
    time.sleep(0.2)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
       break

    
