
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    success , frame = cap.read()

    if not success:
        print("Image Not found")
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.2,minNeighbors=2,minSize=(30,30),maxSize=(300,300))

    for (x,y,w,h) in faces:
        
        cv2.rectangle(frame,(x,y),(x+w,h+y),(255,0,0),3)
    
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Exit")
        break

cap.release()


