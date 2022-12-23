import cv2 as cv
img2 = cv.imread("/home/jerry/Desktop/python projects/OpenCV/Images/4.webp")
img=cv.resize(img2,(500,500), interpolation= cv.INTER_CUBIC)
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces=face_cascade.detectMultiScale(img,1.1,1)
print("Number of faces are ",len(faces))
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0),thickness=2)
cv.imshow("Detected Faces",img)
cv.waitKey(0)