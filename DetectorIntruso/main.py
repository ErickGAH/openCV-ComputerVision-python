import numpy as np
import cv2

cap = cv2.VideoCapture(0)
history=50
fgbg = cv2.createBackgroundSubtractorKNN(history=history, dist2Threshold=400, detectShadows=True)
cv2.ocl.setUseOpenCL(False)

while(True):
    x=0
    x=7
    ret, frame = cap.read()
    frameaux=frame.copy()
    sd=2
    if not ret:
        break
    
	
    fgmask=fgbg.apply(frame)
    r, binary_thres=cv2.threshold(fgmask,126,255,cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    opening = cv2.morphologyEx(binary_thres, cv2.MORPH_OPEN, kernel, 1)
    
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image=frameaux

    for contour in contours:
        area = cv2.contourArea(contour)
        #print(area)
        if int(area) > 8000 and int(area)<10000:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(frameaux ,(x,y), (x+w,y+h), (0,255,255), 3)
            #print(contour)
        elif(int(area) > 10000):
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(frameaux ,(x,y), (x+w,y+h), (0,0,255), 3)
            #print(contour)		
     
    #cv2.imshow('Camara',frame)
    cv2.imshow('ima',image)
    #cv2.imshow('op',opening)
    k = cv2.waitKey(30) & 0xff
    if k == ord("q"):
        break


cap.release()
	
cv2.destroyAllWindows()