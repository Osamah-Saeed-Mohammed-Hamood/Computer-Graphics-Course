import cv2 as cv

img = cv.imread('d:\Osama Al-Jabali\photo_5897520711008895809_x.jpg')

print(img.shape)
img_resize =cv.resize(img,(820,500),interpolation=cv.INTER_CUBIC)

# interpolation=cv.INTER_CUBIC:

# هذا المعامل يحدد الطريقة (الخوارزمية) المستخدمة في إعادة التحجيم.
# cv.INTER_CUBIC:
# خوارزمية تعتمد على الاستيفاء (Interpolation) باستخدام المكعبات.
# تتميز بأنها تعطي جودة عالية خاصة عند تكبير الصورة.

print (img_resize.shape)
cv.imshow("image",img)
cv.imshow("image resize",img_resize)
cv.waitKey(0)
cv.destroyAllWindows()