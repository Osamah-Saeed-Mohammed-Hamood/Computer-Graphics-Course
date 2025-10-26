import numpy as np
import cv2 as cv

def Translate (img,x,y):
    transmatrex=np.float32([[1,0,x],[0,1,y]])
    diementions  = (img.shape[1],img.shape[0])
    return cv.warpAffine(img , transmatrex,diementions)

img = cv.imread('d:\Osama Al-Jabali\photo_5897520711008895809_x.jpg')
cv.imshow("Image",img)

img_translate = Translate(img,-100,-100)

cv.imshow("Translate",img_translate)

# Flipping

flip = cv.flip(img,-1) # 1 => y-axis  , 0 => x-axis  , -1 => x-axis and y-axis
cv.imshow("Flip",flip)

cv.waitKey(0)
cv.destroyAllWindows()