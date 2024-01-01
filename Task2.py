import cv2
#import numpy as np
img = cv2.imread("images/Tom - Copy.jpg")
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgMedian = cv2.medianBlur(img,5)
#Filtered image
imgFilter=cv2.bilateralFilter(img,13,16,16)
#sharped image
imgsharped = cv2.addWeighted(img,2,imgBlur ,-1,0)

cv2.imshow("real Image" , img)
cv2.imshow("Blurred Image" , imgMedian)
cv2.imshow("Filtered Image", imgFilter)
cv2.waitKey(0)