import cv2 as cv

# # image read

# img=cv.imread(r'd:\Osama Al-Jabali\photo_5897520711008895809_x.jpg')

# cv.imshow('image',img)

# cv.waitKey(0)

# cv.destroyAllWindows()

##############################

# # vedio read 

# caption = cv.VideoCapture('d:\Osama Al-Jabali\IMG_20241109_194914_882.mp4')

# while True:
#     isTrue,frame=caption.read()

#     if isTrue:
#         cv.imshow('Video',frame)
#         if cv.waitKey(20) & 0xFF == ord('x'):
#             break
#     else:
#         break
# caption.release()
# cv.destroyAllWindows()

##############################

# Camera Feed Reading

vid = cv.VideoCapture(0)

while True:
    isTrue , frame = vid.read()

    cv.imshow('Camers',frame)

    if cv.waitKey(20) & 0xFF == ord('x'):
        break

vid.release()
cv.destroyAllWindows()
