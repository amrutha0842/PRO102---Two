import random
import cv2
import time

start_time = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        global start_time
        result = False
    return img_name

#videoCaptureObject.release()
cv2.destroyAllWindows()

def main():
    while(True):
        if(time.time() - start_time >= 5):
            name = takeSnapshot()

#calling the main function
main()