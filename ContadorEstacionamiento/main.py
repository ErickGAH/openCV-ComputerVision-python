import cv2
import numpy as np

def onTrackBar(x):
    global image
    rect=boxes[2]
    x1,y1=rect[0]
    x2,y2=rect[1]
    roi=image[y1:y2 + 1,x1:x2 +1].copy()
    roiG=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    roiG=cv2.morphologyEx(roiG,cv2.MORPH_OPEN,kernel,iterations=1)
    
    roiG=cv2.adaptiveThreshold(roiG,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,x)
    
    count=cv2.countNonZero(roiG)
    print(count)
    cv2.imshow("roi",roiG)

    
boxes =[
    [(354, 175), (411,198)],
    [(739, 540), (793, 571)],
    [(822, 515), (870, 541)],
    [(550, 535), (606, 561)],
    [(550, 504), (606, 529)],
    [(550, 237), (606, 264)],
    [(358, 595), (411, 616)],
    [(357, 444), (421, 474)],
    [(555, 410), (604, 443)]
]

cv2.namedWindow("Estacionamiento")
cv2.createTrackbar("C","Estacionamiento",25,50,onTrackBar)

image= cv2.imread(r"C:\Users\erick\OneDrive\Documents\Uaslp\tratamiento\ContadorEstacionamiento\3_ContadorEstacionamiento\data\carParkImg.png")

#roiG=cv2.adaptiveThreshold(roiG,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

#kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#roiG=cv2.morphologyEx(roiG,cv2.MORPH_OPEN,kernel,iterations=1)

#cv2.rectangle(image,rect[0],rect[1],(255,0,0),2)


cv2.imshow("Estacionamiento",image)
cv2.waitKey(0)
cv2.destroyAllWindows()