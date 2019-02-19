import cv2

fistCascade = cv2.CascadeClassifier('D:\\Dev\\virtualcontroller\\src\\haar\\fist.xml')

cam = cv2.VideoCapture(0)

while True:
  ret, img = cam.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = fistCascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

  cv2.imshow('img', img)
  cv2.waitKey(60)
