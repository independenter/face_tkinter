#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui

from tkinter import *
from splider import spliderImpl
import base64,os
from icon import img

class Video_Splider(object):
    def __init__(self):
        # 创建一个窗口
        window = Tk()
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img.encode('utf-8')))
        tmp.close()
        window.iconbitmap('tmp.ico')
        os.remove("tmp.ico")
        window.title("Video Splider")

        # 创建控件
        menubar = Menu(window)
        fmenu1 = Menu(window)
        for item in ['author', 'version', 'author_email']:
            fmenu1.add_command(label=item);

        menubar.add_cascade(label="关于", menu=fmenu1)
        window['menu'] = menubar

        frame=Frame(window)
        frame.pack()

        frame2 = Frame(window)  # 创建框架frame2
        frame2.pack()  # 将frame2放置在window中

        label = Label(frame2, text="Input your url: ")  # 创建标签
        self.url = StringVar()
        entryUrl = Entry(frame2, textvariable=self.url,bg='#F8F8FF')

        download = Button(frame2, text="Download",
                           command=self.downloadBtn)
        online = Button(frame2, text="Online",
                           command=self.onlineBtn)

        self.text = Text(window)
        self.text.pack()
        self.text.insert(END, "Tip\n")
        self.text.insert(END, "支持爱奇艺,腾讯,优酷等,只能在线看哦\n")

        label.grid(row=1, column=1)
        entryUrl.grid(row=1, column=2)
        download.grid(row=1, column=3)
        online.grid(row=1, column=4)

        # 创建一个事件循环，监测事件发生，直到窗口关闭
        window.mainloop()

    def downloadBtn(self):
        print("You have chosen download:" + self.url.get())
        self.text.insert(END, "You have chosen download:" + self.url.get()+"\n")
    def onlineBtn(self):
        url=self.url.get()
        self.text.insert(END, "You have chosen to online:" + url+"\n")
        splider = spliderImpl()
        srcUrl = splider.getUrl(url)



if __name__=='__main__':
    Video_Splider()
