import cv2 as cv
import numpy as np

img = cv.imread('d:\Osama Al-Jabali\WhatsApp2.jpg')

if img is None:
    print("Sorry , This is no photo")
    exit()

height, width, channels = img.shape

binary_img = np.ones((height, width), dtype='uint8')

for i in range(height):
    for j in range(width):
        b, g, r = img[i, j]

        if 45 <= r <= 255 and 34 <= g <= 210 and 20 <= b <= 180:
            binary_img[i, j] = 0
        else:
            binary_img[i, j] = 255

        

# print(binary_img)

skin_img = np.ones_like(img)  # صورة سوداء بنفس أبعاد الصورة الأصلية
skin_img[binary_img == 1] = img[binary_img == 1]  # تطبيق القناع

# عرض الصورة الناتجة
cv.imshow('Original Image', img)
cv.imshow('Skin Color Image', skin_img)

cv.waitKey(0)
cv.destroyAllWindows()