import sys

sys.path.append('C:/py/py37/site-packages')

import cv2

##for image detection

#Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
#trained_face_data = cv2.CascadeClassifier('face_detector.xml')

#Choosing an image to detect faces in 
#img = cv2.imread('elon.png', cv2.IMREAD_UNCHANGED)



#converting to grey scaled
#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces
#face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Drawind rectangles around the faces
#for [x, y, w, h] in face_coordinates: 
	#cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
#print(face_coordinates)



#cv2.imshow('elon', img)
#cv2.waitkey(0)



#print("Code completed")




#for webcam face-detection



#importing the trained datasets
trained_face_data = cv2.CascadeClassifier('face_detector.xml')

#To capture videos from webcam
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)




#Iterate forever over frames
while True:
	
	#Read the current frame
	successful_frame_read, frame = webcam.read()

	#Converting to grayscale
	grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	#Detect faces
	face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

	#Draw rectangles around the faces
	for (x, y, w, h) in face_coordinates:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0,256, 0), 2)

	cv2.imshow('webcam', frame)
	key = cv2.waitKey(1)

	#stop if Q key is pressed
	if key==81 or key==113:
		break






























