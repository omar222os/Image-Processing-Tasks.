import cv2 as cv
import numpy as np

###########################################
count = 0
############################################

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
while True:

    success, img = cap.read()
    cv.imshow("Result", img)

    if cv.waitKey(1) & 0xFF == ord('g'):
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cv.imshow("Gray image",img)
        cv.waitKey(500)
    elif cv.waitKey(1) & 0xFF == ord('h'):
        img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        cv.imshow("HSV image",img)
        cv.waitKey(500)
    elif cv.waitKey(1) & 0xFF == ord('o'):
        cv.imshow("Original image",img)
        cv.waitKey(500)

    elif  cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite("Scanned/image no" + str(count) + ".jpg" ,img)
        cv.rectangle(img,(0,200),(640,300),(0,255,0),cv.FILLED)
        cv.putText(img,"Scan Saves",(150,265),cv.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv.imshow("Result",img)
        cv.waitKey(500)
        count += 1
    elif cv.waitKey(1) & 0xFF == ord('q'):
        break