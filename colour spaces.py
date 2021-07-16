import cv2 as cv

img=cv.imread('/home/vyper/Documents/codes/opencv/photos/boston.jpg')

# BGR to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


# BGR to Hue-Saturation-Value
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

#BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)

# matplotlib doesnt read bgr images so treats like rgb, better to use cv.imshow than plt
# 
# all the above conversions work inverse (GRAY2BGR,HSV2BGR,LAB2BGR) 