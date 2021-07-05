import cv2 as cv
import numpy as np

img=cv.imread('/home/vyper/Documents/codes/opencv/photos/group 2.jpg')

#Translation

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])

    return cv.warpAffine(img,transMat,dimensions)

# -x - left
# -y - up
# x - right
# y - down


translated=translate(img,-100,-100)

cv.imshow('Translated',translated)
cv.waitKey(0)


def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
# -ve - clockwise, +ve - anti-clockwise
cv.imshow('Rotated',rotated)
cv.waitKey(0)