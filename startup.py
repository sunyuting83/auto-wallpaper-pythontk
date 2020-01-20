import os
import sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0])) # 获取当前程序目录
pybin = '%s%s' % (dirname, '/venv/bin/python ') # 定义python虚拟环境
pyapp = '%s%s' % (dirname,  '/app.py') # 定义启动程序
command = '%s%s' % (pybin, pyapp) # 定义启动命令

def checkRcLocal():
    rcLocal = '/etc/rc.local'
    rt = 0
    with open(rcLocal, "r") as fo:
        rc = fo.readlines()
        for i in rc:
            if dirname not in i:
                rt = 0
            else:
                rt = 1
    return rt

def checkStart():
    pcommand = "ps -ef | grep %s | grep -v grep" % pybin
    b = os.popen(pcommand).readlines()
    if len(b) == 0:
        return 0
    else:
        return 1

def SetStart(status):
    rclocal = '/etc/rc.local'
    if status is 0:
        #  删除开机启动
        try:
            with open(rclocal,'r') as r:
                lines=r.readlines()
            with open(rclocal,'w') as w:
                for l in lines:
                    if command not in l:
                        w.write(l)
            return 0
        except Exception as e:
            print(e)
            return 3
    if status is 1:
        # 写入开机启动
        try:
            with open(rclocal, "r") as fp:
                lines = []
                for line in fp: 
                    lines.append(line)
                flin = len(lines) - 1
                lines.insert(flin, command + '\n') # 在第二行插入
                item = ('').join(lines)
                # print(lines,item)
                
            with open(rclocal, 'w+') as fw:
                fw.write(item)
            return 1
        except Exception as e:
            print(e)
            return 3
