import hashlib

import pymysql
#链接数据库需要先导入库
from main.utils import get_md5
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
		VALUES ('1','1','limingfeng','"""+get_md5('li1026ones')+"""','李明锋',0);
	"""
	insert_user_sql2="""
		INSERT INTO `user` (`id`,`group_id`,`account`,`pwd`,`nick_name`,`sex`) 
		VALUES ('2','1','songanqi','"""+get_md5('123456')+"""','宋安琪',1);
	"""
	insert_user_sql3="""
		INSERT INTO `user` (`id`,`group_id`,`account`,`pwd`,`nick_name`,`sex`) 
		VALUES ('3','2','test','"""+get_md5('test')+"""','测试',0);
	"""
	batch_sql(cursor,insert_user_sql1,insert_user_sql2,insert_user_sql3)



def insert_data1(cursor):
    ###################account#####################
    
    insert_account_sql1="""
        INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`remark`, `create_time`,`modify_time`)
        VALUES ('1','1','0','现金', '0', "",'1568131425','1568131425');
    """
    insert_account_sql2="""
        INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`remark`, `create_time`,`modify_time`)
        VALUES ('2','1','1','银行卡1026', '0', "",'1568131425','1568131425');
    """
    insert_account_sql3="""
        INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`remark`, `create_time`,`modify_time`)
        VALUES ('3','1','2','信用卡7680', '0', "",'1568131425','1568131425');
    """
    insert_account_sql4="""
        INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`remark`, `create_time`,`modify_time`)
        VALUES ('4','1','3','微信', '0', "",'1568131425','1568131425');
    """
    insert_account_sql5="""
        INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`remark`, `create_time`,`modify_time`)
        VALUES ('5','1','3','支付宝', '0', "",'1568131425','1568131425');
    """
    insert_account_sql6="""
        INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`remark`, `create_time`,`modify_time`)
        VALUES ('6','1','4','蚂蚁财富', '0', "",'1568131425','1568131425');
    """
    batch_sql(cursor,insert_account_sql1,insert_account_sql2,insert_account_sql3,insert_account_sql4,insert_account_sql5,insert_account_sql6)

    ###################category#####################

    insert_category_sql1="""
        INSERT INTO `category` (`id`,`name`,`type`)
        VALUES ('1','职业',0);
    """
    insert_category_sql2="""
        INSERT INTO `category` (`id`,`name`,`type`)
        VALUES ('2','投资',0);
    """
    insert_category_sql3="""
        INSERT INTO `category` (`id`,`name`,`type`)
        VALUES ('3','其他',0);
    """
    insert_category_sql4="""
        INSERT INTO `category` (`id`,`name`,`type`)
        VALUES ('7','日常餐饮',1);
    """
    insert_category_sql5="""
        INSERT INTO `category` (`id`,`name`,`type`)
        VALUES ('4','衣服饰品',1);
    """
    insert_category_sql6="""
        INSERT INTO `category` (`id`,`name`,`type`)
        VALUES ('5','居家物业',1);
    """
    batch_sql(cursor,insert_category_sql1,insert_category_sql2,insert_category_sql3,insert_category_sql4,insert_category_sql5,insert_category_sql6)

    ###################category_sub#####################

    insert_category_sub_sql1="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('1','工资',1);
    """
    insert_category_sub_sql2="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('2','奖金',1);
    """
    insert_category_sub_sql3="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('3','股票',2);
    """
    insert_category_sub_sql4="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('4','基金',2);
    """
    insert_category_sub_sql5="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('5','平账',3);
    """
    insert_category_sub_sql6="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('6','其他',3);
    """
    batch_sql(cursor,insert_category_sub_sql1,insert_category_sub_sql2,insert_category_sub_sql3,insert_category_sub_sql4,insert_category_sub_sql5,insert_category_sub_sql6)


    insert_category_sub_sql1="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('7','餐饮',7);
    """
    insert_category_sub_sql2="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('8','水果零食',7);
    """
    insert_category_sub_sql3="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('9','衣服',8);
    """
    insert_category_sub_sql4="""
        INSERT INTO `category_sub` (`id`,`name`,`pid`)
        VALUES ('10','包包饰品',8);
    """

    batch_sql(cursor,insert_category_sub_sql1,insert_category_sub_sql2,insert_category_sub_sql3,insert_category_sub_sql4)

	
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



#python3中不支持mysqldb
conn=pymysql.connect(host=DATABASES['default']['HOST'],user=DATABASES['default']['USER'],passwd=DATABASES['default']['PASSWORD'],db=DATABASES['default']['NAME'],port=int(DATABASES['default']['PORT']),charset=DATABASES['default']['CHARSET'])
print('init db')
cursor=conn.cursor() #控制光标
print('cursor:',cursor)
init_db(cursor)
clear_data(cursor)
insert_data(cursor)
insert_data1(cursor)
show_data(cursor)
print('exit')
conn.commit()#提交事务
conn.close()# 断开与数据库的链接


