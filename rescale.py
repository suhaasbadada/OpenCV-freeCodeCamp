import cv2 as cv

img=cv.imread('/home/vyper/Documents/codes/opencv/photos/cat_large.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.5):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)

    dimensions=(height,width)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


def changeRes(height,width):
    #Live Video
    capture.set(4,height)
    capture.set(3,width)

#cv.imshow('Resized',rescaleFrame(img))
#cv.waitKey(0)


capture=cv.VideoCapture('/home/vyper/Documents/codes/opencv/videos/dog.mp4')
while True:
    isTrue,frame=capture.read()

    frame_resized=rescaleFrame(frame)

    cv.imshow('Video Resized',frame_resized)

    if isTrue:     
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()



