import os 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#  also median,gussian filtering


def callback(input):
    pass
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def callback(x):
    pass

def avgfilter():
    root = os.getcwd()
    imgpath = os.path.join(root, 'data', 'cats.png')
    img = cv.imread(imgpath)

    window = 'avg filter'
    cv.namedWindow(window, cv.WINDOW_NORMAL) 
    cv.createTrackbar('n', window, 1, 100, callback)

    h, w, _ = img.shape
    scale = 0.5   
    img = cv.resize(img, (int(w*scale), int(h*scale)))

    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        n = cv.getTrackbarPos('n', window)

        if n < 1:
            n = 1
        if n % 2 == 0:
            n += 1

        imgfilter = cv.blur(img, (n, n))
        cv.imshow(window, imgfilter)

    cv.destroyAllWindows()



if __name__=="__main__":
    avgfilter()