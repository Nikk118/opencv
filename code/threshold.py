import os 
import cv2 as cv 
import matplotlib.pyplot as plt
# also contain image gradient
# edge canny detcection

def threshold():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','cats.png')    
    img=cv.imread(imgpath)
    imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)  
    hist=cv.calcHist([imgGray],[0],None,[256],[0,256])
    plt.figure()
    plt.plot(hist)
    plt.show()

    threshopt=[cv.THRESH_BINARY,cv.THRESH_MASK,cv.THRESH_BINARY_INV,cv.THRESH_TRUNC,cv.THRESH_TOZERO,cv.THRESH_TOZERO_INV]
    threshTitle=["binary","mask","binary_inv","trunc","tozero","tozero_inv"]
    plt.figure()
    plt.subplot(231)
    plt.imshow(imgGray)
    for i in range(len(threshTitle)):
        plt.subplot(2,3,i+1)
        _,imgthresh=cv.threshold(imgGray,70,255,threshopt[i])
        plt.imshow(imgthresh,cmap='gray')
        plt.title(threshTitle[i])
    plt.show()

# image gradient there are also type in this 
def imagegradient():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','car.webp')    
    img=cv.imread(imgpath)
    imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)  
    plt.figure()
    plt.subplot(221)
    plt.imshow(imgGray,cmap='gray')

    laplacian=cv.Laplacian(imgGray,cv.CV_64F,ksize=21)
    plt.subplot(222)
    plt.imshow(laplacian,cmap='gray')
    plt.show()

def cannyedge():
    root=os.getcwd()
    imgpath=os.path.join(root,'data','car.webp')    
    img=cv.imread(imgpath)
    imgGray=cv.cvtColor(img,cv.COLOR_BGR2RGB) 

    h,w,_=imgGray.shape
    scale=0.5
    h=int(h*scale)
    w=int(w*scale)
    img=cv.resize(imgGray,(w,h),interpolation=cv.INTER_LINEAR)

    winame='canny'
    cv.namedWindow(winame)
    cv.createTrackbar('min',winame,0,255,lambda x:None)
    cv.createTrackbar('max',winame,0,255,lambda x:None)
    while True:
        if cv.waitKey(1)&0xFF==ord('q'):
            break
        minval=cv.getTrackbarPos('min',winame)
        maxval=cv.getTrackbarPos('max',winame)
        imgcanny=cv.Canny(img,minval,maxval)
        cv.imshow(winame,imgcanny)

    cv.destroyAllWindows()

if __name__=="__main__":
    # threshold()
    # imagegradient()
    cannyedge()