#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

#frame库
import traceback
from tkinter import *
from icon import img
import base64,time
#程序库
try:
    import face_recognition
except Exception as e:
    traceback.print_exc(file=open('error.log', 'w+'))
import cv2
import os


class Face_recognition_frame(object):
    def __init__(self):
        #print("识别程序初始化")
        # 创建一个窗口
        window = Tk()
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img.encode('utf-8')))
        tmp.close()
        window.iconbitmap('tmp.ico')
        os.remove("tmp.ico")
        window.title("Face Recognition")

        # 创建控件
        menubar = Menu(window)
        fmenu1 = Menu(window)
        for item in ['author:Dob', 'version:1.0.0', 'author_email:m15501951002@163.com']:
            fmenu1.add_command(label=item)

        menubar.add_cascade(label="关于", menu=fmenu1)
        window['menu'] = menubar

        frame = Frame(window)
        frame.pack()

        frame2 = Frame(window)  # 创建框架frame2
        frame2.pack()  # 将frame2放置在window中

        label = Label(frame2, text="粘贴人物库文件夹路径: ")  # 创建标签
        self.path = StringVar()
        entryPath = Entry(frame2, textvariable=self.path, bg='#F8F8FF')

        recognition = Button(frame2, text="识别", command=self.startRecognition)

        self.text = Text(window)
        self.text.pack()
        self.text.insert(END, "Tip:\n") #使用技巧

        label.grid(row=1, column=1)
        entryPath.grid(row=1, column=2)
        recognition.grid(row=1, column=3)

        # 创建一个事件循环，监测事件发生，直到窗口关闭
        window.mainloop()

    def startRecognition(self):
        # 这是一个超级简单（但很慢）的例子，在你的网络摄像头上实时运行人脸识别
        # PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
        # 请注意：这个例子需要安装OpenCV
        # 具体的演示。如果你安装它有困难，试试其他不需要它的演示。
        # 得到一个参考的摄像头# 0（默认）
        video_capture = cv2.VideoCapture(0)
        # 加载示例图片并学习如何识别它。
        path = self.path.get()  # 一般在同级目录下的images文件中放需要被识别出的人物图
        total_image = []
        total_image_name = []
        total_face_encoding = []
        try:
            for fn in os.listdir(path):  # fn 表示的是文件名
                total_face_encoding.append(
                    face_recognition.face_encodings(face_recognition.load_image_file(path + "/" + fn))[0])
                fn = fn[:(len(fn) - 4)]  # 截取图片名（这里应该把images文件中的图片名命名为为人物名）
                total_image_name.append(fn)  # 图片名字列表
            while True:
                # 抓取一帧视频
                ret, frame = video_capture.read()
                # 发现在视频帧所有的脸和face_enqcodings
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)
                # 在这个视频帧中循环遍历每个人脸
                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    # 看看面部是否与已知人脸相匹配。
                    for i, v in enumerate(total_face_encoding):
                        match = face_recognition.compare_faces([v], face_encoding, tolerance=0.4)
                        name = "Unknown"
                        if match[0]:
                            name = total_image_name[i]
                            break
                    # 画出一个框，框住脸
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    # 画出一个带名字的标签，放在框下
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                # 显示结果图像
                cv2.imshow('Face_Recognition', frame)
                # 按b退出
                if cv2.waitKey(1) & 0xFF == ord('b'):
                    break
            # 释放摄像头中的流
            video_capture.release()
            cv2.destroyAllWindows()
        except FileNotFoundError as e:
            self.text.insert(END,"您可能没有输入人物库路径"+'\n')
            self.text.insert(END, time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))+"detail:" + e.__str__()+'\n')
        except IndexError as e:
            self.text.insert(END,"人物库某张单图可能存在2个人脸"+'\n')
            self.text.insert(END, time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))+"detail:" + e.__str__()+'\n')



if __name__ == '__main__':
    Face_recognition_frame()