import  cv2
# this is my webcam 0
cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, back = cap.read() # here i am simply reading , ret - was the reading of web cam sucessul r not, back is the image what the opencv is reading
    if ret:
        cv2.imshow("image", back)
    if cv2.waitKey(5) == ord('q'): # ord value givivng unicord of q, wait key to wait fro that particular amount of time
    # save the image
         cv2.imwrite('image.jpg', back)
         break

cap.release()
cv2.destroyAllWindows()
