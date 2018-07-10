import pymysql
#2.插入操作
db= pymysql.connect(host="localhost",user="root",
 	password="root",db="test",port=3306,use_unicode=True, charset="utf8")
 
# 使用cursor()方法获取操作游标
cur = db.cursor()
 
sql_insert ="insert into user(id,name,password) values(3,'新','1234')"
 
try:
	cur.execute(sql_insert)
	#提交
	db.commit()
except Exception as e:
	print (e)
	#错误回滚
	db.rollback() 
finally:
	db.close()