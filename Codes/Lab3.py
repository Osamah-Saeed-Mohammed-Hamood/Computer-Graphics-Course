import cv2 as cv

img = cv.imread('d:\Osama Al-Jabali\photo_5897520711008895809_x.jpg')
print (img.shape)
img_croped = img[0:200,0:300]

cv.imshow("image",img)
cv.imshow("image croped",img_croped)

cv.waitKey(0)
cv.destroyAllWindows()