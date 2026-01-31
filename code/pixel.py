import cv2 as cv
import matplotlib.pyplot as plt
import os 



def readAndWrite():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')
    img=cv.imread(imgpath)
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    plt.figure()
    plt.title("original")
    plt.imshow(imgRGB)
    plt.show()

    eyeRegion = imgRGB[180:230, 40:90]

    h, w, _ = eyeRegion.shape

    # Paste location
    start_y = 20
    start_x = 20

    imgRGB[start_y:start_y+h, start_x:start_x+w] = eyeRegion
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()



if __name__=="__main__":
    readAndWrite()
  