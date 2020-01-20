#!/usr/bin/python
# -*- coding: UTF-8 -*-
from urllib.request import urlopen
import requests
import os
import sys
import time
from contextlib import closing
import logging

logging.basicConfig(level=logging.INFO,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='download.log',
        filemode='a')

from apscheduler.schedulers.blocking import BlockingScheduler

class SetWallpaper():
	def __init__(self,outime):
		# 下载目录变量
		self.rootpath = os.path.join(os.getcwd(),'download')
		self.db = os.path.join(os.getcwd(),'last.key')

		# 新建scheduler
		scheduler = BlockingScheduler()

		print(outime)

		if outime == '0':
			time.sleep(300)
			self.startWall()

		elif outime == '1':
			# 间隔5小时执行一次
			try:
				# print(u'here')
				scheduler.add_job(func=self.startWall, trigger='cron', hours='*/5')
				# 这里的调度任务是独立的一个线程
				scheduler._logger = logging # 记录log
				scheduler.start()
			except Exception as e:
				print(e)
				pass

		elif outime == '2':
			# 间隔1小时执行一次
			# scheduler.add_job(func=self.startWall, trigger='cron', hours='*/1')
			# 这里的调度任务是独立的一个线程
			scheduler.add_job(func=self.startWall, trigger='cron', second='*/5')
			scheduler._logger = logging # 记录log
			scheduler.start()
    
	# 测试开始
	def textS(self):
		import datetime
		print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '你好')
	
	# 开始
	def startWall(self):
		# 下载目录变量
		self.rootpath = os.path.join(os.getcwd(),'download')
		# 检测网络
		checkNet = self.checkNetWorks()
		if checkNet == False:
			return
		# 检测目录是否存在或创建目录
		checkP = self.checkPath()
		if checkP:
			return self.checkFirstPic()

	# 检测网络
	def checkNetWorks(self):
		url = "http://www.baidu.com"
		try:
			status = requests.get(url).status_code
			if status == 200:
				return True
		except Exception as e:
			return False

	# 检测下载目录
	def checkPath(self):
		if os.path.isdir(self.rootpath) == False:
			os.mkdir(self.rootpath)
		if os.path.isfile(self.db) == False:
			os.mknod(self.db)
		return True

	# 检查下载目录
	def checkFirstPic(self):
		lists = os.listdir(self.rootpath)
		lslen = len(lists)
		if lslen == 0:
			# 如果目录为空 请求api
			self.keys = 'first'
			return self.getapi()
		# filepath = os.path.join(self.rootpath,lists[-1])
		# keys, ext = os.path.splitext(filepath)
		# keys = keys.split('/')[-1]
		# self.keys = self.makeKey(keys)
		with open(self.db, "r") as fo:
			self.keys = fo.read()
			return self.getapi()
	
	def makeKey(self,keys):
		k = keys.split('.')[0]
		if '-' in k:
			return k.split('-')[0]
		if '_' in k:
			return k.split('_')[0]


	# 请求接口
	def getapi(self):
		parem = self.keys
		geturl = 'http://wallpaper.zhenguohe.com/?key=%s' % parem
		if parem == 'first':
			geturl = 'http://wallpaper.zhenguohe.com/'
		try:
			req = requests.get(geturl).content.decode("utf-8")
			filename = req.split('/')[-1]
			return self.download(req,filename)
		except Exception as e:
			print(e)
			return False

	# 下载函数
	def download(self, down_url, down_name):
		allPath = os.path.join(self.rootpath, down_name)
		if os.path.isfile(allPath):
			return
		with closing(requests.get(down_url, stream=True)) as r:
			rc = r.status_code
			if 299 < rc or rc < 200:
				print ('returnCode%s\t%s' % (rc, down_url))
				'''
				在这里更新url错误状态入库
				'''
				return
			try:
				with open(allPath, 'wb') as f:
					for data in r.iter_content(1024):
						f.write(data)
			except Exception as e:
				print (e)
				pass
		keys = self.makeKey(down_name)
		with open(self.db, "r+") as fo:
			fo.write(keys)
		self.setWall(allPath)

	# 设置壁纸
	def setWall(self,pic):
		try:
			os.system('gsettings set org.gnome.desktop.background picture-uri "%s"' % str(pic))
			return
		except Exception as e:
			print (e)
			return

if __name__ == '__main__':
	otime = (sys.argv[1])
	SetWallpaper(otime)
