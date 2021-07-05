import cv2 as cv

img=cv.imread('/home/vyper/Documents/codes/opencv/photos/cat_large.jpg')
cv.imshow('Cat',img)

cv.waitKey(0)

capture=cv.VideoCapture('/home/vyper/Documents/codes/opencv/videos/dog.mp4')

while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)

    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()