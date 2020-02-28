
import cv2
import connect_db as conn
import os

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False




# counting the numbers
def insert_new_record():
    roll_num = input("Enter Your Roll Number: ")
    name = input("Enter Your Name: ")
    if (is_number(roll_num) and name.isalpha()):
        insert = '''
                           insert into dumy_student(name,roll_num) values(%s,%s) returning id
                       '''
        record = [name, roll_num]
        conn.cursor.execute(insert, record)
        id = conn.cursor.fetchone()

        conn.connection.commit()
        record.append(id[0])

        return record  #returing new created record


    else:
        if (is_number(roll_num)):
            print("Enter Alphabetical Name")
        if (name.isalpha()):
            print("Enter Numeric Roll number")




# Take image function

def takeImages():
    rec=insert_new_record()#inserting new record
    cam = cv2.VideoCapture(0)
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    sampleNum = 0

    while (True):

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # incrementing sample numberrecord=insert_new_record()
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder TrainingImag
            cv2.imwrite("TrainingImage" + os.sep + rec[0] + "." + str(rec[2]) + '.' +
                        str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            # display the frame
            cv2.imshow('frame', img)
        # wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 100
        #elif sampleNum > 40:
         #   break
    cam.release()
    cv2.destroyAllWindows()
    print("save detials succes")

takeImages()
