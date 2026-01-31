# hsv color space

# hue(type os color) ,saturation(concentration),value(intensity of color)

import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def hsvsolorsegmentaion():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


    lowerbound = np.array([35, 50, 50])
    upperbound = np.array([85, 255, 125])
    mask=cv.inRange(hsv,lowerbound,upperbound)

    plt.figure()
    plt.imshow(mask)
    plt.show()


def imageResize():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath) 
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

    img=img[145:225,125:230,:]
    print(img.shape)
    h,w,_=img.shape

    scale=1/4
    print("1")

    interMethods=[
        cv.INTER_AREA,
        cv.INTER_NEAREST,
        cv.INTER_CUBIC,
        cv.INTER_LANCZOS4
    ]
    print("1")

    interpTitle=["area","nearest","cublic","lanczos4"]

    plt.figure()

    plt.subplot(2,3,1)
    print("1")
    plt.imshow(img)
    print("1")

    imageResize=cv.resize(img,(int(w*0.25),int(h*0.25)),
                          interpolation=cv.INTER_LANCZOS4)
    plt.imshow(imageResize)

    # for i in range(len(interMethods)):
    #     plt.subplot(2,3,i+2)
    #     imageResize=cv.resize(img,(int(w*scale),int(h*scale)),
    #     interpolation=interMethods[i])        
    #     plt.imshow(imageResize)
    #     plt.title(interpTitle[i])
    plt.show()

    


if __name__=="__main__":
    # hsvsolorsegmentaion()
    imageResize()

