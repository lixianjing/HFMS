import pymysql
#链接数据库需要先导入库
from main.settings import DATABASES

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

def clear_table(cursor):
	print('clear_table')
	table_list=('test','user_group','user','account','category','category_sub','record')
	for item in table_list:
		try:
			cursor.execute('DROP TABLE '+item)
		except Exception as err:
			print('err:',err)


def create_table(cursor):
	print('create_table')
	create_test_sql="""
		CREATE TABLE test (
  		_id int(10) unsigned NOT NULL AUTO_INCREMENT,
  		id int(10) unsigned unique NOT NULL,
  		name text ,
  		PRIMARY KEY (_id)
		) COMMENT = '测试表';
	"""

	create_user_group_sql="""
		CREATE TABLE user_group (
  		_id int(10) unsigned NOT NULL AUTO_INCREMENT,
  		id int(10) unsigned unique  NOT NULL,
  		name varchar(200) NOT NULL comment '用户组名称',
    	avatar  text comment '头像路径',
  		auth int(2) unsigned default 0 comment '权限字段',
    	PRIMARY KEY (_id)
		) COMMENT = '用户组表';
	"""

	create_user_sql="""
		CREATE TABLE user (
  		_id int(10) unsigned NOT NULL AUTO_INCREMENT,
  		id int(10) unsigned unique  NOT NULL,
  		group_id int(10) unsigned  NOT NULL,
  		account varchar(100)   NOT NULL,
  		pwd varchar(100)  NOT NULL,
  		nick_name varchar(200) NOT NULL comment '用户名称',
    	avatar  text comment '头像路径',
		phone varchar(20),
  		sex int(2) unsigned default 0 comment '性别0男人，1女人',
  		auth int(2) unsigned default 0 comment '权限字段',
    	PRIMARY KEY (_id)
		) COMMENT = '用户表';
	"""
	create_account_sql="""
		CREATE TABLE account (
  		_id int(10) unsigned NOT NULL AUTO_INCREMENT,
  		id int(10) unsigned unique  NOT NULL,
  		uid int(10) unsigned NOT NULL,
  		type int(2) unsigned default 0 comment '0现金，1银行卡，2信用卡，3.虚拟账号，4.投资账户',
  		name varchar(200)   NOT NULL comment '账户名称',
  		balance  float default 0 comment '账户金额',
		remark  text comment '备注',
  		create_time long NOT NULL,
  		modify_time long NOT NULL,
    	PRIMARY KEY (_id)
		) COMMENT = '账户表';
	"""
	create_category_sql="""
		CREATE TABLE category (
  		_id int(10) unsigned NOT NULL AUTO_INCREMENT,
  		id int(10) unsigned unique  NOT NULL,
  		name varchar(200)   NOT NULL comment '目录名称',
  		type int(2)  unsigned NOT NULL  comment '目录类型 0收入，1支出，2转账，3，借出，4.借入，5，还出，6，还入',
    	PRIMARY KEY (_id)
		) COMMENT = '目录表';
	"""
	create_category_sub_sql="""
		CREATE TABLE category_sub(
  		_id int(10) unsigned NOT NULL AUTO_INCREMENT,
  		id int(10) unsigned unique  NOT NULL,
  		pid int(10) unsigned NOT NULL,
  		name varchar(200)   NOT NULL comment '目录名称',
    	PRIMARY KEY (_id)
		) COMMENT = '目录子表';
	"""
	create_record_sql="""
		CREATE TABLE record (
	  	_id int(10) unsigned NOT NULL AUTO_INCREMENT,
	  	id int(10) unsigned unique NOT NULL,
	   	cate_id int(10) unsigned NOT NULL comment '类型id',
	   	uid int(10) unsigned  NOT NULL comment '用户id',
	   	account_id int(10) unsigned NOT NULL comment '账户id',
	   	type int(2) unsigned  default 0 comment '关联类型 默认为0，0为手动输入，1为文案输入',
	   	type_id int(10) unsigned   comment '数据记录id',
	   	amount float unsigned default 0 comment '价格',
	   	remark  text comment '备注',
	   	occur_time long NOT NULL,
	   	status int(2) unsigned default 0 comment '状态0， 1不可用',
	  	PRIMARY KEY (_id)
		) COMMENT = '消费记录表';
	"""

	batch_sql(cursor,create_test_sql,create_user_group_sql,create_user_sql,create_account_sql,create_category_sql,create_category_sub_sql,create_record_sql)
	

	
		

host='149.248.5.135'
port=3306
user='lucien'
pd='shui'
database_name='hfms'
charset='utf8'

host_local='127.0.0.1'
user_local='root'
pd_local='shui'

#python3中不支持mysqldb
#conn=pymysql.connect(host=host,user=user,passwd=pd,db=database_name,port=port,charset=charset)
conn=pymysql.connect(host=host_local,user=user_local,passwd=pd_local,db=database_name,port=port,charset=charset)
print('init db')
cursor=conn.cursor() #控制光标
print('cursor:',cursor)
init_db(cursor)
clear_table(cursor)
create_table(cursor)
print('exit')
conn.commit()#提交事务
conn.close()# 断开与数据库的链接


