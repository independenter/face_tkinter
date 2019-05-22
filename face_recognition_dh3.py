#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import face_recognition

#输入已知图片
known_image1 = face_recognition.load_image_file("images/donghui.jpg")
known_image2 = face_recognition.load_image_file("images/obama.jpg")
#输入待识别的图片
unknown_image = face_recognition.load_image_file("images/donghui.jpg")

known_encoding1 = face_recognition.face_encodings(known_image1)[0]
known_encoding2 = face_recognition.face_encodings(known_image2)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_encoding1,known_encoding2], unknown_encoding)
#输出的results是一串Boolean值
print(results.index(True))