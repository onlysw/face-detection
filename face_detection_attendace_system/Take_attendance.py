import datetime
import os
import time
import cv2 as cv
def recognize_attendence():
    ids=[]
    recognizer = cv.face_LBPHFaceRecognizer.create()
    recognizer.read("Trained_data"+os.sep+"Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv.CascadeClassifier(harcascadePath)
    cam = cv.VideoCapture(0)
    font = cv.FONT_HERSHEY_SIMPLEX

    while True:
        ret, im = cam.read()
        gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if Id not in ids:
                ids.append(Id)

            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(
                    ts).strftime('%H:%M:%S')
                tt = str(Id)
            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv.imwrite("ImagesUnknown" + os.sep + "Image" + str(noOfFile) +
                            ".jpg", im[y:y + h, x:x + w])
            cv.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        cv.imshow('im', im)
        if (cv.waitKey(1) == ord('q')):
            break


    return ids


ids=recognize_attendence()
print(ids)
