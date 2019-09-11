
##账户表###############################################
###建表字段
CREATE TABLE `account` (
  `_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id` int(10) unsigned unique  NOT NULL,
  `uid` int(10) unsigned NOT NULL,
  `type` int(2) unsigned default 0 comment '0现金，1银行卡，2信用卡，3.虚拟账号，4.投资账户',
  `name` varchar(200)   NOT NULL comment '账户名称',
  `balance`  float default 0 comment '账户金额',
  `desc` text  comment '账户描述',
  `create_time` long NOT NULL ,
  `modify_time` long  NOT NULL,
    PRIMARY KEY (`_id`)
) COMMENT = '账户表';
###操作字段
INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`desc`, `create_time`,`modify_time`) 
VALUES ('1','1','0','现金', '0', "",'1568131425','1568131425');
INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`desc`, `create_time`,`modify_time`) 
VALUES ('2','1','1','银行卡1026', '0', "",'1568131425','1568131425');
INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`desc`, `create_time`,`modify_time`) 
VALUES ('3','1','2','信用卡7680', '0', "",'1568131425','1568131425');
INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`desc`, `create_time`,`modify_time`) 
VALUES ('4','1','3','微信', '0', "",'1568131425','1568131425');
INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`desc`, `create_time`,`modify_time`) 
VALUES ('5','1','3','支付宝', '0', "",'1568131425','1568131425');
INSERT INTO `account` (`id`,`uid`, `type`, `name`, `balance`,`desc`, `create_time`,`modify_time`) 
VALUES ('6','1','4','蚂蚁财富', '0', "",'1568131425','1568131425');

##用户组表#############################################
###建表字段
CREATE TABLE `user_group` (
  `_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id` int(10) unsigned unique  NOT NULL,
  `name` varchar(200) NOT NULL comment '用户组名称',
    `avatar`  text comment '头像路径',
  `auth` int(2) unsigned default 0 comment '权限字段',
    PRIMARY KEY (`_id`)
) COMMENT = '用户组表';
###操作字段
####插入
INSERT INTO `user_group` (`id`,`name`) 
VALUES ('1','李明锋&宋安琪');
INSERT INTO `user_group` (`id`,`name`) 
VALUES ('2','test');

##用户表#################################################
###建表字段
CREATE TABLE `user` (
  `_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id` int(10) unsigned unique  NOT NULL,
  `group_id` int(10) unsigned  NOT NULL,
  `account` varchar(100)   NOT NULL,
  `pwd` varchar(100)  NOT NULL,
  `nick_name` varchar(200) NOT NULL comment '用户名称',
    `avatar`  text comment '头像路径',
  `sex` int(2) unsigned default 0 comment '性别0男人，1女人',
  `auth` int(2) unsigned default 0 comment '权限字段',
    PRIMARY KEY (`_id`)
) COMMENT = '用户表';
###操作字段
####插入
INSERT INTO `user` (`id`,`group_id`,`account`,`pwd`,`nick_name`,`sex`) 
VALUES ('1','1','limingfeng','123456','李明锋',0);
INSERT INTO `user` (`id`,`group_id`,`account`,`pwd`,`nick_name`,`sex`) 
VALUES ('2','1','songanqi','654321','宋安琪',1);
INSERT INTO `user` (`id`,`group_id`,`account`,`pwd`,`nick_name`,`sex`) 
VALUES ('3','2','test','123456','测试账号',1);

##目录表#################################################
###建表字段
CREATE TABLE `category` (
  `_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id` int(10) unsigned unique  NOT NULL,
  `name` varchar(200)   NOT NULL comment '目录名称',
  `type` int(2)  unsigned NOT NULL  comment '目录类型 0收入，1支出，2转账，3，借出，4.借入，5，还出，6，还入',
    PRIMARY KEY (`_id`)
) COMMENT = '目录表';
###操作字段
####插入
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('1','职业收入',0);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('2','投资收入',0);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('3','其他收入',0);

INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('7','日常餐饮',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('4','衣服饰品',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('5','居家物业',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('6','行车交通',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('8','交流通信',1);

INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('9','休闲娱乐',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('10','学习进修',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('11','人情往来',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('12','医疗保健',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('13','其他杂项',1);

INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('14','转账',2);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('15','借出',3);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('16','借入',4);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('17','还出',5);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('18','还入',6);

##目录子表#################################################
###建表字段
CREATE TABLE `category_sub` (
  `_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id` int(10) unsigned unique  NOT NULL,
  `pid` int(10) unsigned NOT NULL,
  `name` varchar(200)   NOT NULL comment '目录名称',
    PRIMARY KEY (`_id`)
) COMMENT = '目录子表';
###操作字段
####插入
INSERT INTO `category` (`id`,`name`,`pid`) 
VALUES ('1','职业收入',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('2','投资收入',0);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('3','其他收入',0);

INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('7','日常餐饮',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('4','衣服饰品',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('5','居家物业',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('6','行车交通',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('8','交流通信',1);

INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('9','休闲娱乐',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('10','学习进修',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('11','人情往来',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('12','医疗保健',1);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('13','其他杂项',1);

INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('14','转账',2);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('15','借出',3);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('16','借入',4);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('17','还出',5);
INSERT INTO `category` (`id`,`name`,`type`) 
VALUES ('18','还入',6);








##消费记录表
CREATE TABLE `item` (
  `_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id` int(10) unsigned unique NOT NULL,
  `cate_id` int(10) unsigned NOT NULL comment '类型id',
  `uid` int(10) unsigned  NOT NULL comment '用户id',
  `type` int(2) unsigned  zerofill  NOT NULL comment '关联类型 默认为0，0为手动输入，1为文案输入',
  `type_id` int(10) unsigned   comment '数据记录id',
  `account_id` int(10) unsigned NOT NULL comment '账户id',
  `amount` float unsigned zerofill NOT NULL comment '价格',
  `desc` text DEFAULT NULL,
  `occur_time` timestamp NOT NULL,
  `status` int(2) unsigned zerofill  NOT NULL  comment '状态0， 1不可用',
  `original_id`  int(10) unsigned NOT NULL,
  PRIMARY KEY (`_id`)
) COMMENT = '消费记录表';

insert