import cv2 as cv

HAAR_FILE = "haarcascade_frontalface_default.xml"
cascade = cv.CascadeClassifier(HAAR_FILE)

cap = cv.VideoCapture(1)

sum_person = 0
while(True):
    ret, frame = cap.read()

    face = cascade.detectMultiScale(frame)

    for x, y, w, h in face:
        sum_person += 1
        print(sum_person)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)

    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()