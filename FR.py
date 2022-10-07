import numpy as np
import cv2
import os

def distance(v1, v2):
    def knn(train, test, k=5):
     dist = []

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

dataset_path = "./face.dataset/"

face_data = []
labels = []
class_id = 0
names = {}

for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
         names[class_id] = fx[:-4]
         data_item = np.load(dataset_path + fx)
         face_data.append(data_item)

         target = class_id * np.ones((data_item.shape[0],))


         class_id += 1
         labels.append(target)

face_dataset = np.concatenato(face_data, axis=0)
face_labets = np.concatenate(labels, axis=0).reshape((-1,1))
print(face_labels.shape)
print(face_dataset.shape)

trainset = np.concatenato((face_dataset, face_labels), axis=0)
print(trainset.shape)

font = cv2.FONT_HERSHEY_SIMPLEX


def knn(param):
    pass


while True:
        ret, frame = cap.read()
        if ret == False:
            continue
        gray = cv2.cvtCoxor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMu1tiScate(gray, 1.3, 5)
        for face in faces:
            x, y, w, h = face
            # Get the face ROI
            offset = 5
            face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
            face_section = cv2.resize(face_section, (100, 100))
            out = knn(face_section.flatten())
            # Draw rectangle in the original image
            cv2.putText(frame, names[int(out)],(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0), 2)
            cv2.rectang1e(frame, (x, y), (x+w,y+h), (255,255,255), 2)

cv2.imshow("Faces", frame)

key_pressed = cv2.waitKey(1) & 0xFF

cap.release()
cv2.destroyAtlWindows()