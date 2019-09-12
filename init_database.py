import pymysql
#链接数据库需要先导入库

def batch_sql(cursor,*sqls):
	for sql in sqls:
		try:
			cursor.execute(sql)
		except Exception as err:
			print('sql:',sql,'err:',err)		
		

def init_db(cursor):
	print('init_db')
	try:
		cursor.execute('set character_set_database=utf8')
	except Exception as err:
		print('err:',err)

def clear_data(cursor):
	print('clear_table')
	table_list=('test','user_group','user','account','category','category_sub','record')
	for item in table_list:
		try:
			cursor.execute('delete from '+item)
		except Exception as err:
			print('err:',err)

def insert_data(cursor):
	print('insert_data')
	###################test#####################
	insert_test_sql="""
		INSERT INTO test (id,name) 
		VALUES (1,'测试')
	"""
	batch_sql(cursor,insert_test_sql)

	###################user_group#####################
	insert_user_group_sql1="""
		INSERT INTO user_group (id,name) 
		VALUES ('1','李明锋&宋安琪');
	"""
	insert_user_group_sql2="""
		INSERT INTO user_group (id,name) 
		VALUES ('2','测试组1');
	"""
	insert_user_group_sql3="""
		INSERT INTO user_group (id,name) 
		VALUES ('3','测试组2');
	"""

	batch_sql(cursor,insert_user_group_sql1,insert_user_group_sql2,insert_user_group_sql3)
	
	###################user#####################
	insert_user_sql1="""
		INSERT INTO `user` (`id`,`group_id`,`account`,`pwd`,`nick_name`,`sex`) 
		VALUES ('1','1','limingfeng','123456','李明锋',0);
	"""
	insert_user_sql2="""
		INSERT INTO `user` (`id`,`group_id`,`account`,`pwd`,`nick_name`,`sex`) 
		VALUES ('2','1','songanqi','123456','宋安琪',1);
	"""
	insert_user_sql3="""
		INSERT INTO `user` (`id`,`group_id`,`account`,`pwd`,`nick_name`,`sex`) 
		VALUES ('3','2','test','123456','测试',0);
	"""
	batch_sql(cursor,insert_user_sql1,insert_user_sql2,insert_user_sql3)

	###################account#####################

	insert_account_sql1="""
		INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`remark`, `create_time`,`modify_time`) 
		VALUES ('1','1','0','现金', '0', "",'1568131425','1568131425');
    """
    insert_account_sql2="""
    	pppp
    """
    print("test:",insert_account_sql2)

	# batch_sql(cursor,insert_account_sql1,insert_account_sql2)
	
def show_data(cursor):
	print('show_data')
	###################test#####################
	show_test_sql="""
		SELECT * FROM test;
	"""
	cursor.execute(show_test_sql)	
	print("data:",cursor.fetchone())  

	###################user_group#####################
	show_user_group_sql="""
		SELECT * FROM user_group;
	"""
	cursor.execute(show_user_group_sql)	
	print("data:",cursor.fetchone())  
	
	###################user#####################
	show_user_sql="""
		SELECT * FROM user;
	"""
	cursor.execute(show_user_sql)	
	print("data:",cursor.fetchone())  
	
	###################account#####################
	show_account_sql="""
		SELECT * FROM account;
	"""
	cursor.execute(show_account_sql)	
	print("data:",cursor.fetchone())  
	
	###################category#####################
	show_category_sql="""
		SELECT * FROM category;
	"""
	cursor.execute(show_category_sql)	
	print("data:",cursor.fetchone())  
	
	###################category_sub#####################
	show_category_sub_sql="""
		SELECT * FROM category_sub;
	"""
	cursor.execute(show_category_sub_sql)	
	print("data:",cursor.fetchone())  

	###################record#####################
	show_record_sql="""
		SELECT * FROM record;
	"""
	cursor.execute(show_record_sql)	
	print("data:",cursor.fetchone())  
	
	
	
	
		
host='149.248.5.135'
port=3306
user='lucien'
pd='shui'
database_name='hfms'
charset='utf8'


#python3中不支持mysqldb
conn=pymysql.connect(host=host,user=user,passwd=pd,db=database_name,port=port,charset=charset)
print('init db')
cursor=conn.cursor() #控制光标
print('cursor:',cursor)
init_db(cursor)
clear_data(cursor)
insert_data(cursor)
show_data(cursor)
print('exit')
conn.commit()#提交事务
conn.close()# 断开与数据库的链接


