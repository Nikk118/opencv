import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def purecolor():
    zeros=np.zeros((100,100))
    ones=np.ones((100,100))
    bimg=cv.merge((zeros,zeros,255*ones))
    gimg=cv.merge((zeros,255*ones,zeros))
    rimg=cv.merge((255*ones,zeros,zeros))

    plt.figure()
    plt.subplot(231)
    plt.imshow(bimg)
    plt.title("blue")
  
    plt.subplot(233)
    plt.imshow(rimg)
    plt.title("red")

    plt.subplot(232)
    plt.imshow(gimg)
    plt.title("green")
    plt.show()


def bgrchannelGray():
    root = os.getcwd()
    imgpath = os.path.join(root, 'data', 'cats.png')
    img = cv.imread(imgpath)

    if img is None:
        print("Image not found")
        return

    b, g, r = cv.split(img)

    zero = np.zeros_like(b)

    plt.subplot(131)
    bimg = cv.merge((b, zero, zero))
    plt.imshow(bimg)

    plt.subplot(132)
    gimg = cv.merge((zero, g, zero))
    plt.imshow(gimg)

    plt.subplot(133)
    rimg = cv.merge((zero, zero, r))   
    plt.imshow(rimg)

    plt.show()

# gray scale images
# single channel (black and white pixel)

def grayscale():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath)
    imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",imgGray)
    cv.waitKey(0)


def readasgray():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath,cv.IMREAD_GRAYSCALE)
    cv.imshow("gray",img)
    cv.waitKey(0)

if __name__=="__main__":
    # purecolor()
    # bgrchannelGray()
    # grayscale()
    readasgray()