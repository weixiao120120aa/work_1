#coding:utf-8
import sys  # 提供了许多函数和变量来处理 Python 运行时环境的不同部分.

reload(sys)
sys.setdefaultencoding('GBK')

import pymysql
conn = pymysql.connect("localhost","root","120120aa","test")

cur = conn.cursor()

def insert(username,password):
	sql = "insert into user (username,password) values ('%s','%s')" %(username,password)
	cur.execute(sql)
	conn.commit()
	conn.close()

def isExisted(username,password):
	sql="select * from user where username ='%s' and password ='%s'" %(username,password)
	cur.execute(sql)
	result = cur.fetchall()
	if (len(result) == 0):
		return False
	else:
		return True


