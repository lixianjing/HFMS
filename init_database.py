import pymysql
#链接数据库需要先导入库


def init_db(cursor):
	print('init_db')
	try:
		cursor.execute('set character_set_database=utf8')
	except Exception as err:
		print('err:',err)

def clear_table(cursor):
	print('clear_table')
	try:
		cursor.execute('DROP TABLE test')
	except Exception as err:
		print('err:',err)

	# cursor.execute('DROP TABLE user')
	# cursor.execute('DROP TABLE account')
	# cursor.execute('DROP TABLE category')
	# cursor.execute('DROP TABLE category_sub')
	# cursor.execute('DROP TABLE item')
	pass

def create_table(cursor):
	create_user_group_sql="""
		CREATE TABLE user_group (
  	_id int(10) unsigned NOT NULL AUTO_INCREMENT,
  	id int(10) unsigned unique  NOT NULL,
  	name varchar(200) NOT NULL comment '用户组名称',
    avatar  text comment '头像路径',
  	auth int(2) unsigned default 0 comment '权限字段',
    PRIMARY KEY ('_id')
) COMMENT = '用户组表'
	"""

	create_test_sql="""
	CREATE TABLE test (
  _id int(10) unsigned NOT NULL AUTO_INCREMENT,
  id int(10) unsigned unique NOT NULL,
  name text ,
  PRIMARY KEY (_id)
) COMMENT = '测试表';
	"""


	cursor.execute(create_test_sql)

	# cursor.execute('DROP TABLE user')
	# cursor.execute('DROP TABLE account')
	# cursor.execute('DROP TABLE category')
	# cursor.execute('DROP TABLE category_sub')
	# cursor.execute('DROP TABLE item')
	pass

def insert_data(cursor):
	print('insert_data')
	insert_test_sql="""
		INSERT INTO test (id,name) 
		VALUES (1,'测试')
	"""
	cursor.execute(insert_test_sql)
	
def show_data(cursor):
	print('show_data')
	show_test_sql="""
		SELECT * FROM test;
	"""
	cursor.execute(show_test_sql)	
	results = cursor.fetchall()
	print("id","name")  
	#遍历结果  
	for row in results :  
		id = row[1]  
		name = row[2]
		print(id,name)  

#python3中不支持mysqldb
conn=pymysql.connect(host='149.248.5.135',user='lucien',passwd='shui',db='hfms',port=3306,charset='utf8')
#这里要注意port 后要跟随数字，不要写出成port="3306"
#charset 中的utf8 写成“utf-8”会报错
print('init db')
cursor=conn.cursor() #控制光标
# cursor.execute(sql语句)
print('cursor:',cursor)
init_db(cursor)
clear_table(cursor)
create_table(cursor)
insert_data(cursor)
show_data(cursor)
print('exit')
conn.commit()#提交事务
conn.close()# 断开与数据库的链接


