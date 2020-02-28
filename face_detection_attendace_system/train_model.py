import os
import cv2 as cv
import numpy as np
from PIL import Image

def getImageLabel(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    #defilinf empty list of id and face
    faces=[]
    Ids=[]

    for imgpath in imagePaths:
        #loading image from diretory
        image=Image.open(imgpath)
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(image, 'uint8')
        # getting the Id from the image
        Id = int(os.path.split(imgpath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)

    return  faces,Ids

#defining train fuction

def TrainImages():
    recognizer = cv.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv.CascadeClassifier(harcascadePath)
    faces, Id = getImageLabel("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("Trained_data"+os.sep+"Trainner.yml")
    print("Images Trained")
    return Id



id=TrainImages()

print(id)
