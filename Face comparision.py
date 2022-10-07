# Python program for face
# comparison
'''
import cv2
from __future__ import print_function, unicode_literals
from facepplib import FacePP, exceptions

# define global variables
face_detection = ""
faceset_initialize = ""
face_search = ""
face_landmarks = ""
dense_facial_landmarks = ""
face_attributes = ""
beauty_score_and_emotion_recognition = ""


# define face comparing function
def face_comparing(app, Image1, Image2):
    print()
    print('-' * 30)
    print('Comparing Photographs......')
    print('-' * 30)

    cmp_ = app.compare.get(image_url1=Image1,
                           image_url2=Image2)

    print('Photo1', '=', cmp_.image1)
    print('Photo2', '=', cmp_.image2)

    # Comparing Photos
    if cmp_.confidence > 70:
        print('Both photographs are of same person......')
    else:
        print('Both photographs are of two different persons......')


# Driver Code
if __name__ == '__main__':

    # api details
    api_key = 'xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret = 'TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

    try:

        # call api
        app_ = FacePP(api_key=api_key,
                      api_secret=api_secret)
        funcs = {
            face_detection,
            #face_comparing_localphoto,
            #face_comparing_websitephoto,
            faceset_initialize,
            face_search,
            face_landmarks,
            dense_facial_landmarks,
            face_attributes,
            beauty_score_and_emotion_recognition
        }

    img = cv2.imread('img44.jpeg')
    img1 = cv2.imread('img45.jpeg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    haar_cascade = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml')
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Detected faces', img)
    cv2.imshow('Detected faces', img1)
    cv2.waitKey(0)

    # Pair 1kk
        image1 = 'https://i.postimg.cc/FRRvV32k/img44.jpg'
        image2 = 'https://i.postimg.cc/DzYvDxQP/img45.jpg'
        face_comparing(app_, image1, image2)

        image1 = 'https://i.postimg.cc/WpHXvwF3/images.jpg'
        image2 = 'https://i.postimg.cc/Sst7mmK5/download.jpg'
        face_comparing(app_, image1, image2)


        # Pair2
        image1 = 'https://i.postimg.cc/2yNDRM1h/img210.jpg'
        image2 = 'https://i.postimg.cc/Y9YSW1gN/img117.jpg'
        face_comparing(app_, image1, image2)

    except exceptions.BaseFacePPError as e:
        print('Error:', e)
'''
# Importing OpenCV package
import cv2

# Reading the image
img = cv2.imread('images.jpg')

# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml')

# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)
