# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:36:50 2022

@author: T
"""
import cv2
Known_width = 15
Known_distance = 122
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
fonts = cv2.FONT_HERSHEY_COMPLEX

# Reading the image
img = cv2.imread(r"G:\opencv\ref_120.jpg")
  
# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier(r"C:\Users\T\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
  
# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
face_width=0  
# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    face_width = w
#cv2.imshow('Detected faces', img)
print(face_width)
cv2.imwrite(r"G:\opencv\det_faces.jpg",img)

focal_length = (face_width * Known_distance) / Known_width
print(focal_length)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
 
# looping through frame, incoming from
# camera/video
while True:
 
    # reading the frame from camera
    frame = cv2.imread(r"G:\opencv\ref_52.jpg")
    
    
 
    # calling face_data function to find
    # the width of face(pixels) in the frame
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    haar_cascade = cv2.CascadeClassifier(r"C:\Users\T\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
  
# Applying the face detection method on the grayscale image
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
    face_width_in_frame=0  
# Iterating through rectangles of detected faces
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_width_in_frame = w
        
 
    # check if the face is zero then not
    # find the distance
    if face_width_in_frame != 0:
       
        # finding the distance by calling function
        # Distance distance finder function need
        # these arguments the Focal_Length,
        # Known_width(centimeters),
        # and Known_distance(centimeters)
        Distance = ((face_width_in_frame * Known_distance) / Known_width)/3.8
        
 
        # draw line as background of text
        cv2.line(frame, (30, 30), (230, 30), RED, 32)
        cv2.line(frame, (30, 30), (230, 30), BLACK, 28)
 
        # Drawing Text on the screen
        cv2.putText(
            frame, f"Distance: {round(Distance,2)} CM", (30, 35),
          fonts, 0.6, GREEN, 2)
 
    # show the frame on the screen
    cv2.imshow("frame", frame)
    cv2.imwrite(r"G:\opencv\det_dist.jpg",frame)
    # quit the program if you press 'q' on keyboard
    break
 
# closing the camera



#cv2.waitKey(0)