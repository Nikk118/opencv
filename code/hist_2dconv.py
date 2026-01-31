import os 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def grayHist():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath,cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.imshow(img)

    hist=cv.calcHist([img],[0],None,[256],[0,256])
    plt.figure()
    plt.plot(hist)
    plt.xlabel("bins")
    plt.ylabel("pixel")
    plt.show()


def colorHist():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img=img[156:167,34:156,:]
    plt.figure()
    plt.imshow(img)

    color=['b','r','g']
    plt.figure()
    for i in range(len(color)):
        hist=cv.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist,color[i])
    plt.xlabel("intensity")
    plt.ylabel("pixel")
    plt.show()



def convolution2d():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath)
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)

    n=100

    kernel=np.ones((n,n),np.float32)/(n*n)

    imgfilter=cv.filter2D(imgRGB,-1,kernel)

    plt.figure()
    plt.subplot(121)
    plt.imshow(imgRGB)

    plt.subplot(122)
    plt.imshow(imgfilter)
    plt.show()


if __name__=="__main__":
    # grayHist()
    # colorHist()
    convolution2d()

