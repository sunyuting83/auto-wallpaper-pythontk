import os
# db = os.path.join(os.getcwd(),'last.db')
# with open(db, "r+") as fo:
#     fo.write('00a43cd2458a4562cf1dffd4d2bfdb9f')
# string_switch(db,"0054dada8159f42ac1345cdceab7c054","tasting","g")
# os.system('gsettings set org.gnome.desktop.background picture-uri "%s"' % str(pic))

# coding:utf-8
'''
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test():
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '你好')


scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, trigger='cron', second='*/5')
scheduler.start()
'''
# rootpaht = str(os.getcwd()) # 获取当前程序目录
# pyapp = '%s%s' % (rootpaht,  '/app.py') # 定义启动程序
# pybin = '%s%s' % (rootpaht, '/venv/bin/python ')
# pcommand = "ps -ef | grep %s | grep -v grep" % pybin
# b = os.popen(pcommand).readlines()
# print(b)
'''
# 写入开机启动
with open('data.txt', "r") as fp:
    lines = []
    for line in fp: 
        lines.append(line)
    flin = len(lines) - 1
    lines.insert(flin, 'a new line\n') # 在第二行插入
    item = ('').join(lines)
    # print(lines,item)
    
with open('data.txt', 'w+') as fw:
    fw.write(item)
'''  
#     s = '\n'.join(lines)
#     fp.write(s)
'''
#  删除开机启动
with open('data.txt','r') as r:
    lines=r.readlines()
with open('data.txt','w') as w:
    for l in lines:
       if 'a new line' not in l:
          w.write(l)
'''
'''
import sys

if __name__ == '__main__':
    # 提升到root权限
    if os.geteuid():
        args = [sys.executable] + sys.argv
        # 下面两种写法，一种使用su，一种使用sudo，都可以
        os.execlp('su', 'su', '-c', ' '.join(args))
        # os.execlp('sudo', 'sudo', *args)

    # 从此处开始是正常的程序逻辑
    print('Running at root privilege. Your euid is', os.geteuid())
'''
import sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0])) 
print(os.path.realpath(sys.argv[0]))
print(dirname, filename)

dirname, filename = os.path.split(os.path.abspath(sys.argv[0])) # 获取当前程序目录
pybin = '%s%s' % (dirname, '/venv/bin/python ') # 定义python虚拟环境
pyapp = '%s%s' % (dirname,  '/app.py') # 定义启动程序
command = '%s%s' % (pybin, pyapp) # 定义启动命令
print(command)