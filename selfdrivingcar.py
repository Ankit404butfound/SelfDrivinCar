import serial           #For serial communication with arduino
import cv2              #For image recognition
import numpy as np      #For same
import urllib.request   #For accessing image through phone
  
ser = serial.Serial('COM8', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)  #Change COM8 to COM port to which Arduino is connected
cap = cv2.VideoCapture(0) 
red_light_cascade = cv2.CascadeClassifier(r'C:\Users\pc\...PATH TO RED LIGHT CASCADE.xml')#Train the cascade 
yellow_light_cascade = cv2.CascadeClassifier(r'C:\Users\pc\...PATH TO YELLO LIGHT CASCADE.xml')#Same
url="http://192.168.43.1:8080/shot.jpg"     #Gather image from this url
scaling_factor =0.5
dist = 0
fact = 0
count1 = 0
count2 = 0
while True:
        imglink=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp,-1)
        frame = cv2.resize(img, None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
        redlight = red_light_cascade.detectMultiScale(frame, 1.3, 2)
        yellowlight = yellow_light_cascade.detectMultiScale(frame, 1.3, 2)
        for (x,y,w,h) in redlight:         #Detect red light
                cv2.rectangle(frame, (x-fact,y-fact), ((x+w)-fact,(y+h)-fact), (3400,1234,2500), 1)
                dist = ((37.05*400)/(h))+30
                dist = str(int(dist))
                print(dist)
                count2 = 0
                count1 += 1
                cv2.putText(frame,"Teddy"+str(int(dist))+"cm",(x, y), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0), 2)
        for (x,y,w,h) in yellowlight:      #Detect green light
                cv2.rectangle(frame, (x-fact,y-fact), ((x+w)-fact,(y+h)-fact), (3400,1234,2500), 1)
                dist = ((37.05*500)/(h))+30
                dist = str(int(dist))
                print(dist)
                count1 = 0
                count2 += 1
                cv2.putText(frame,"Fan"+str(int(dist))+"cm",(x, y), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0), 2)
        
        if count1 == 1:
            ser.write(b"r")                #Write 'r' to serial if red is detected, check arduino code
        if count2 == 1:
            ser.write(b"y")                #Write 'y' to serial if yellow is detected,
        else:
            ser.write(b"g")
        cv2.imshow('Ankit Raj', frame)
        c = cv2.waitKey(25)
