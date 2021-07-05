import cv2 as cv

img=cv.imread('/home/vyper/Documents/codes/opencv/photos/group 2.jpg')

# Converting to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Blur
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

#Cascade
canny=cv.Canny(img,125,175)

#Dilating image
dilated=cv.dilate(canny,(3,3),iterations=1)

#Eroding
eroded=cv.erode(dilated,(3,3),iterations=1)

#Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)


#Cropping
cropped=img[50:200,200:400]


cv.imshow('functions',cropped)
cv.waitKey(0)