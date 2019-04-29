# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time   : 2019/4/29 9:24
# @Author : WuZe
# @Desc   : 
# ==================================================

import sys
import os
import cv2

face_cascade = cv2.CascadeClassifier(r'../data/haarcascade_frontalface_default.xml')
imagepath = r'../file/1.jpg'
image = cv2.imread(imagepath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5),
    flags=cv2.CASCADE_SCALE_IMAGE
)
for (x, y, w, h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    # cv2.circle(image, ((x + x + w) / 2, (y + y + h) / 2), w / 2, (0, 255, 0), 2)
cv2.imshow("Find Faces!", image)
cv2.waitKey(0)
