import os
import sys
from tkinter import messagebox

def clean():
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0])) # 获取当前程序目录
    rootpath = os.path.join(dirname,'download')
    db = os.path.join(dirname,'last.key')

    if not os.path.isfile(db):
        pass
    else:
        os.remove(db)

    if not os.path.isdir(rootpath):  # os.path.isdir()函数判断某一路径是否为目录
        pass         #直接删除文件
    else:
        files = os.listdir(rootpath);   #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        for file in files:
            filePath = os.path.join(rootpath, file);  #拼接路径
            #这一步很重要 主要作用是拼接目录下的目录
            if os.path.isfile(filePath):     #判断filepath是否为文件
                os.remove(filePath);         #删除文件
            elif os.path.isdir(filePath):    #得到当前目录下的目录
                clean(filePath);         #删除文件夹
        os.rmdir(rootpath);
        # os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以,
        # 否则, 抛出OSError。
    messagebox.showinfo('提示消息', '清除成功！')
