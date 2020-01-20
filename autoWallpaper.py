#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from tkinter import *  # 使用Tkinter前需要先导入
from tkinter import messagebox
from tkinter import ttk
# from PIL import ImageTk # 解决linux的icon问题
import subprocess

import base64

from clean import clean
from startup import checkRcLocal, checkStart, SetStart
# from app import SetWallpaper

class APP:
    def __init__(self, master):
        self.window = master
        t = self.window
        t.title('每日美女壁纸')
        t.resizable(0,0)  # 大小不可变
        # 设置图标.py可用
        # Icon = './Icon/girl_128.ico'
        # img = ImageTk.PhotoImage(file=Icon)
        # t.tk.call('wm', 'iconphoto', t._w, img)
            
        #创建frame容器
        frmLA = Frame(width=330, height=20)
        frmLB = Frame(width=330, height=20)
        frmLC = Frame(width=330, height=20)
        frmLD = Frame(width=330, height=52)
        frmLE = Frame(width=330, height=30)
        frmLF = Frame(width=330, height=50)

        frmLA.grid(row=0, column=0,padx=10,pady=10)
        frmLB.grid(row=1, column=0,padx=10)
        frmLC.grid(row=2, column=0,padx=10,pady=8)
        frmLD.grid(row=3, column=0,padx=10,pady=10)
        frmLE.grid(row=4, column=0,padx=10)
        frmLF.grid(row=5, column=0,padx=10)

        checkB = IntVar(checkRcLocal())  # 定义var1整型变量用来存放选择行为返回值

        # 添加开机启动
        def setStart():
            status = SetStart(checkB.get())
            if status is 1:
                messagebox.showinfo('提示消息', '设置开机启动成功')
            elif status is 0:
                messagebox.showinfo('提示消息', '取消开机启动成功')
            elif status is 3:
                messagebox.showinfo('提示消息', '发生错误')

        if checkB is 1:
            # print('11')
            checkBtn = Checkbutton(
                frmLA, text='开机启动',
                variable=checkB,
                onvalue=0, 
                offvalue=1,
                font=('Arial', 11),
                command=setStart
            )
        else:
            # print('00')
            checkBtn = Checkbutton(
                frmLA, text='开机启动',
                variable=checkB,
                onvalue=1, 
                offvalue=0,
                font=('Arial', 11),
                command=setStart
            ) 
         # 传值原理类似于radiobutton部件
        checkBtn.grid(row=0,column=0,sticky = E+W)

        # 添加提示文本
        TStext = Label(frmLB,
            text='提示：如果不设置开机启动，重启后无法自动更换壁纸', 
            font=('Arial', 10),
            fg='blue'
        )
        TStext.grid(row=0,column=0,sticky = E+W)
        # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

        # 添加下拉菜单
        # 创建一个下拉列表
        number = StringVar()
        numberChosen = ttk.Combobox(frmLC, width=16, textvariable=number)
        numberChosen['values'] = (u'每天',u'5小时',u'1小时')     # 设置下拉列表的值
        numberChosen.grid(column=0, row=0,sticky = E+W)      # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        # 说明文字
        Cotext = Label(frmLC,
            text='选择更换时间', 
            font=('Arial', 11),
            fg='blue'
        )
        Cotext.grid(row=0,column=1,sticky = E+W, padx=10)

        #添加清空按钮
        btnClean = Button(frmLD, 
            text='清空壁纸缓存', 
            width = 11,
            height = 2,
            font=('Arial', 11),
            relief = 'raised',
            command=lambda:clean()
        )#在frmLF容器中添加
        btnClean.grid(row=0,column=0,sticky = E+W)

        # 添加提示文本
        TStext = Label(frmLE,
            text='提示：清空壁纸缓存后，将从第一张开始更换', 
            font=('Arial', 10),
            fg='blue'
        )
        TStext.grid(row=0,column=0,sticky = E+W)
        # start 开始按钮事件
        def clickMe(n):
            btnSend.configure(state='disabled')
            btnStop.configure(state='normal')
            dirname, filename = os.path.split(os.path.abspath(sys.argv[0])) # 获取当前程序目录
            pybin = '%s%s' % (dirname, '/venv/bin/python') # 定义python虚拟环境
            pyapp = '%s%s' % (dirname,  '/app.py') # 定义启动程序
            outime = numberChosen.get()
            if outime is '每天':
                outime = '0'
            elif outime is '5小时':
                outime = '1'
            else:
                outime = '2'
            # 后台运行app.py
            # command = '%s%s%s%s%s' % ('nohup ', rootbash,' app.py ',outime, ' > nohup.out 2>&1 &')
            # print(command)
            # os.system(command)
            subprocess.Popen([pybin, pyapp, outime])
            # SetWallpaper(outime)
        
        # stop 停止按钮事件
        def stopMe():
            btnSend.configure(state='normal')
            btnStop.configure(state='disabled')
            dirname, filename = os.path.split(os.path.abspath(sys.argv[0])) # 获取当前程序目录
            pybin = '%s%s' % (dirname, '/venv/bin/python ') # 定义python虚拟环境
            pcommand = "ps -ef | grep %s | grep -v grep | awk '{print $2}' | xargs kill -9" % pybin
            os.popen(pcommand)
            print(checkB.get())

        #添加按钮
        btnSend = Button(frmLF, 
            text='开 始', 
            width = 10,
            height = 2,
            state='normal',
            command=lambda:clickMe(number)
        )#在frmLF容器中添加
        btnSend.grid(row=0,column=0,sticky = E+W)
        btnStop = Button(frmLF, 
            text='停 止', 
            width = 10,
            height = 2,
            command=stopMe
        )
        btnStop.grid(row=0,column=1,sticky = E+W,padx=3)
        btnCancel = Button(frmLF, 
            text='退 出', 
            width = 10,
            height = 2,
            command=t.quit
        )
        btnCancel.grid(row=0,column=2,sticky = E+W)

        # 检测app.py是否运行 并定义按钮状态
        st = checkStart()
        if st == 0:
            btnSend.configure(state='normal')
            btnStop.configure(state='disabled')
        else:
            btnSend.configure(state='disabled')
            btnStop.configure(state='normal')

        #添加图片
        # imgInfo = PhotoImage(file = "python_logo.gif")
        # lblImage = Label(frmRT, image = imgInfo)
        # lblImage.image = imgInfo
        # lblImage.grid()

        #固定容器大小
        frmLA.grid_propagate(0)
        frmLB.grid_propagate(0)
        frmLC.grid_propagate(0)
        frmLD.grid_propagate(0)
        frmLE.grid_propagate(0)
        frmLF.grid_propagate(0)


def main():
    # 初始化tk
    window = Tk()
    app = APP(window)
    # 主窗口循环显示
    window.mainloop()


if __name__ == '__main__':
    main()
