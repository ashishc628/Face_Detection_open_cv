#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install opencv-python


# In[2]:


import cv2


# In[3]:


import numpy as np 


# In[ ]:


face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' )
video = cv2.VideoCapture(0)

while True:
    ret , frame=video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_detector.detectMultiScale(gray,1.3)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
video.release()
cv.destroyAllWindows()
vs.stop()


# In[ ]:




