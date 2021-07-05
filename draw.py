import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')    # 3 is the number of colour channels

blank[200:300,300:400]=0,255,0

cv.rectangle(blank,(0,0),(250,500),(255,0,0),thickness=cv.FILLED)

cv.circle(blank,(250,250),40,((0,0,255)),thickness=2)
  

cv.line(blank,(250,250),(500,500),((255,255,255)),thickness=3)

cv.putText(blank,'Drawing',(300,400),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)


cv.imshow('drawing',blank)
cv.waitKey(0)