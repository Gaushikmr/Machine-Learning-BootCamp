
import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

while cap.isOpened():

    ret, frame = cap.read()

    if ret:
        faces = classifier.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 225), 4)


        cv2.imshow("My window", frame)

        key = cv2.waitKey(5)
        print("1-10")

        if key == ord("q"):
            cv2.imwrite("img", frame)
            break



cap.release()
cv2.destroyAllWindows()



