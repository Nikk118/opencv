import numpy as np
import cv2 as cv
import os
def videoFromWeb():
    cap=cv.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Webcam not accessible")
        exit()
    while True:
        ret,frame=cap.read()
        if ret:
            cv.imshow('video',frame)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def videowrite():
    cap=cv.VideoCapture(0)
    fourcc=cv.VideoWriter_fourcc(*'XVID')
    root=os.getcwd()
    outpath=os.path.join(root,'data','webcame.avi')
    out=cv.VideoWriter(outpath,fourcc,20.0,(640,480))
    while cap.isOpened():
        ret,frame=cap.read()
        if ret:
            out.write(frame)
            cv.imshow('video',frame)
        if cv.waitKey(1)==ord('q'):
            break       
    cap.release()
    out.release()
    cv.destroyAllWindows()
    

if __name__=="__main__":
    # videoFromWeb()
    videowrite()