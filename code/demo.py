import cv2 as cv

# if __name__=="__main__":
    # print(cv.__version__)



import os 
# import matplotlib.pyplot as plt
import numpy as np

def readImage():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath)
    cv.imshow('cat',img)
    cv.waitKey(0)

def writeImage():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath)
    savepath=os.path.join(root,'data','cat_copy.png')
    cv.imwrite(savepath,img)
if __name__=="__main__":
    # readImage()
    writeImage()