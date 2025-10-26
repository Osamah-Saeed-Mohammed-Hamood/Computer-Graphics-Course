import cv2 as cv

img = cv.imread('d:\Osama Al-Jabali\photo_5897520711008895809_x.jpg')
cv.imshow("Image",img)

def Rotate(img , angle , rotPoint=None):
    (width,height) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMatrex=cv.getRotationMatrix2D(rotPoint,angle,1.0)

    diemntion = (width,height)

    return cv.warpAffine(img,rotMatrex,diemntion)

rotated = Rotate(img,-90)

cv.imshow("Rotate",rotated)

cv.waitKey(0)
cv.destroyAllWindows()