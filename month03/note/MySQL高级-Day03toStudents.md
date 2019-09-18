# **MySQL-Day02必须掌握**

## **外键**

**原理** 

```
让当前表字段的值在另一张表的范围内去选择
```

**使用规则**

```mysql
1、数据类型要一致
2、主表被参考字段必须为KEY的一种 : PRI
```

**级联动作**

```mysql
1、cascade : 删除 更新同步(被参考字段)
2、restrict(默认) : 不让主表删除 更新
3、set null : 删除 更新,从表该字段值设置为NULL
```

## **嵌套查询（子查询）**

**定义**

```
把内层的查询结果作为外层查询的条件
```

## **多表查询**

**笛卡尔积**

```
多表查询不加where条件,一张表的每条记录分别和另一张表的所有记录分别匹配一遍
```

## **连接查询**

**分类**

```mysql
1、内连接（表1 inner join 表2 on 条件）
2、外连接（表1 left|right join 表2 on 条件）
	1、左连接 ：以左表为主显示查询结果
	2、右连接 ：以右表为主显示查询结果
```

**语法**

```mysql
select 表名.字段名 from 表1 inner join 表2 on 条件；
```

## **锁**

**1、目的** ：解决客户端并发访问的冲突问题

**2、锁分类**

```mysql
1、锁类型 : 
      读锁：读的时候别人不能碰
      写锁：更新的时候别人不能更新，只能一个人更新
2、锁粒度 : 
      行级锁(InnoDB) ：锁粒度小。行之间的
      表级锁(MyISAM)：锁粒度大。表之间的。表级锁会造成程序阻塞。
```

## **数据导入**

**方式一（使用source命令）**
不需要自己创建表，结构式文件
```mysql
mysql> source /home/tarena/xxx.sql
```

**方式二（使用load命令）**
需要自己创建表
```mysql
1、将导入文件拷贝到数据库搜索路径中
   show variables like 'secure%';
2、在数据库中创建对应的表
3、执行数据导入语句
```
乱码
```text
哪个场景的乱码？
1、表乱码（修改表的编码方式）
2、使用load导入或导出的时候容易乱码（打开文件的时候修改编码方式）
```

## **索引**

**定义**

```
对数据库表中一列或多列的值进行排序的一种结构(BTree)
```

**优点**

```mysql
加快数据的检索速度
```

**缺点**

```mysql
1、占用实际物理存储空间
2、索引需动态维护，消耗资源，降低数据的维护速度
```

**分类及约束**

```mysql
1、普通索引（MUL）: 无约束
2、唯一索引（UNI）：字段值不允许重复，但可为NULL
3、主键（PRI）	：字段值不允许重复，不可为NULL
4、外键		 ：让当前表字段的值在另一张表的范围内选择
```

# **MySQL-Day03笔记**

## **存储引擎**
***不要轻易切换存储引擎***

### **定义**

```mysql
处理表的处理器（使数据落地就是存入磁盘的引擎）
```
### **基本操作**

```mysql
1、查看所有存储引擎
   mysql> show engines;
2、查看已有表的存储引擎
   mysql> show create table 表名;
3、创建表指定
   create table 表名(...)engine=MyISAM,charset=utf8,auto_increment=10000;

   mysql> create table test_myisam(id int)engine=MyISAM,charset=utf8;
   mysql> show create table test_myisam;

4、已有表指定
   alter table 表名 engine=InnoDB;
```

### **==常用存储引擎及特点==**

- InnoDB	(默认的存储引擎)	

1. 支持行级锁　　＃＃行之间的影响小
2. 支持外键、事务（跟钱相关的一般都使用事务）、事务回滚
3. 表字段和索引同存储在一个文件中
   1. 表名.frm ：表结构
   2. 表名.ibd : 表记录及索引文件 （聚集：存储数据+索引）（数据结构是B树）

创建innodb_test表检测数据存储结构
```mysql
mysql> use db3;
mysql> create table innodb_test(id int);
mysql> SHOw create table innodb_test;
mysql> insert into innodb_test values(1),(2);
mysql> select * from innodb_test;
```

- MyISAM

1. 支持表级锁
2. 表字段和索引分开存储
   1. 表名.frm ：表结构
   2. 表名.MYI : 索引文件(my index)##叶子节点，不存储数据，存储指向磁盘的物理指针，也就是查询地址。
   3. 表名.MYD : 表记录(my data) 

创建myisam_test表检测数据存储结构
```mysql
mysql> use db3;
mysql> create table myisam_test(id int) engine=MyISAM;
mysql> SHOw create table myisam_test;
mysql> insert into myisam_test values(1),(2);
mysql> select * from myisam_test;
```

- MEMORY

1. 表记录存储在内存中，效率高（hash哈希算法）
*跟B+ ，Ｂ树不在一个量级上,memory查找速度超级快*
2. 服务或主机重启，表记录清除

*可删除的，可有可无的数据可以用内存存储。eg:游戏皮肤，称号。*

创建memory_test1表检测数据存储结构
```mysql
mysql> use db3;
mysql> create table memory_test1(id int) engine=MEMORY;
mysql> SHOw create table memory_test1;
mysql> insert into memory_test1 values(1),(2);
mysql> select * from memory_test1;
```
结果展示
*只限于查看文档类型，不能查看内容，也不要轻易修改。*
```
tarena@tarena:~$ sudo su
[sudo] tarena 的密码： 
root@tarena:/home/tarena# cd /var/lib/mysql
root@tarena:/var/lib/mysql# ls
auto.cnf  db22             ib_buffer_pool  ib_logfile1  mysql_upgrade_info  stu
country   debian-5.7.flag  ibdata1         ibtmp1       performance_schema  sys
db2       dict             ib_logfile0     mysql        spider
root@tarena:/var/lib/mysql# cd db3
root@tarena:/var/lib/mysql/db3# ls
bank.frm    db.opt            memory_test.frm  myisam_test.MYD
bank.ibd    innodb_test.frm   middle.frm       myisam_test.MYI
course.frm  innodb_test.ibd   middle.ibd       teacher.frm
course.ibd  memory_test1.frm  myisam_test.frm  teacher.ibd
```
创建memory_test表检测重启是否会失去数据
```
mysql> use db3;
mysql> create table memory_test(id int) engine=MEMORY;
mysql> SHOw create table memory_test;
mysql> insert into memory_test values(1),(2);
mysql> select * from memory_test;

tarena@tarena:~$ service mysql restart

mysql> select * from memory_test;
Empty set (0.00 sec)
```
**如何选择存储引擎**

```mysql
1、执行查操作多的表用 MyISAM(使用InnoDB浪费资源)

###建议：具体问题具体分析 -->不知道用什么的时候，选择Innodb.
mysql中有key_buffer-->内存中缓存索引，大小为64M-12BM的内存
 M:存索引    In:存索引+数据    两者相比，M的索引数量很大；Innodb也会产生大量的内存交换
 M：A  In：A+数据  IN快
 M：A   AAAAAA  In：A+数据  AAAAAA  M快
 具体情况根据压测结果对待。

2、执行写操作多的表用 InnoDB
3、临时表 ： MEMORY    redis简单，速度快
```

## **MySQL的用户账户管理**

### **开启MySQL远程连接**

**更改配置文件，重启服务！**
#### 1、sudo su
```mysql
tarena@tarena:~$ sudo su
[sudo] tarena 的密码： 
root@tarena:/home/tarena# cd
```
#### 2、cd /etc/mysql/mysql.conf.d
etc：该目录一般会存当前系统（ubantu)的所有安装的软件的配置文件，前提是有超级用户root权限才能打开

```
root@tarena:~# cd /etc/mysql/mysql.conf.d
root@tarena:/etc/mysql/mysql.conf.d# ls
mysqld.cnf  mysqld_safe_syslog.cnf
```
#### 3、cp mysqld.cnf mysqld.cnf.bak
```
root@tarena:/etc/mysql/mysql.conf.d# cp mysqld.cnf mysqld.cnf.bak
root@tarena:/etc/mysql/mysql.conf.d# ls
mysqld.cnf  mysqld.cnf.bak  mysqld_safe_syslog.cnf
root@tarena:/etc/mysql/mysql.conf.d# ll
总用量 32
drwxr-xr-x 2 root root  4096 8月   9 11:31 ./
drwxr-xr-x 4 root root  4096 7月  25 08:26 ../
-rw-r--r-- 1 root root  3052 1月  12  2018 mysqld.cnf
-rw-r--r-- 1 root root  3052 8月   9 11:31 mysqld.cnf.bak
-rw-r--r-- 1 root root 12288 8月   9 11:16 .mysqld.cnf.swp
-rw-r--r-- 1 root root    21 1月  12  2018 mysqld_safe_syslog.cnf
```
#### 4、修改配置文件vi mysqld.cnf 
 
（1） 修改监听地址
```
#找到44行左右, bind-address = 127.0.0.1加 # 注释，变成#bind-address = 127.0.0.1
```
（2）修改编码方式

   修改之前先进行模糊查询：show variables like '%chara%'
```
   找到配置文件，打开，寻找[mysqld]，然后另起一行添加character_set_server = utf8
```
#### 5、保存退出
```
vi使用 : 按a ->编辑文件 ->ESC ->shift+: ->wq
```
#### 6、service mysql restart
```
tarena@tarena:~$ service mysql restart
tarena@tarena:~$ ps aux|grep 'mysql'
```

### **添加授权用户**

1. 用root用户登录mysql
```mysql
   mysql -uroot -p123456
   mysql -uroot -h176.23.4.102 -p
   mysql> select * from mysql.user\G;

*************************** 1. row ***************************
                  Host: localhost
                  User: root

监听本地地址
  终端输入mysql -uroot -p123456
  查看用户select * from mysql.user\G;  host显示localhost；
```
2. 授权
```
   grant 权限列表 on 库.表 to "用户名"@"localhost" identified by "密码" with grant option;
```
**登录地址localhost**
```
localhost表示登录地址。默认是127.0.0.1
当localhost是%时，表示所有的IP都可以登录服务
当localhost是特定IP地址（xixi，但是xixi是不存在的网址）时，不能可以进入服务
当localhost是特定IP地址（内网地址176.23.4.102）时，只有用户通过改地址才可以进入服务
```
3. 刷新权限
```
   flush privileges;
```

**权限列表**

```
all privileges 、select 、insert ... ... 
库.表 ： *.* 代表所有库的所有表
```

### **示例**
**示例一**
#### 1、添加授权用户work,密码123
（1）对**所有库**的**所有表**有**所有权限**
```mysql
  mysql>grant all privileges on *.* to 'work'@'%' identified by '123' with grant option;
  mysql>flush privileges;
  mysql> select * from mysql.user\G;

  *************************** 6. row ***************************
                  Host: %
                  User: work

终端输入mysql -uwork -p123
查看用户select * from mysql.user\G;  host显示%；
可以查看所有的库：show databases;

 ##两种方法都可以登录
mysql -uwork -p
mysql -uwork -h176.23.4.102 -p
```
（2）对**country库**的**sanguo数据表**有**所有权限**：只能看当前的库
```
mysql>grant all privileges on country.sanguo* to 'work1'@'%' identified by '123' with grant option;
  mysql>flush privileges;
  mysql> select * from mysql.user\G;

*************************** 8. row ***************************
                  Host: %
                  User: work1

只能查看country库中的sanguo数据表：show databases;

mysql -uwork1 -p   ##不可以登录
```
#### 2、改变登录地址
（1）添加指定不存在网址
```
  mysql>grant all privileges on *.* to 'xixi'@'xixi' identified by '131227' with grant option;
  mysql>flush privileges;
  mysql> select * from mysql.user\G;

*************************** 7. row ***************************
                  Host: xixi
                  User: xixi

mysql -uxixi -p   ##不可以登录
mysql -uxixi -h176.23.4.102 -p   ##不可以登录
```
（2）添加特定存在网址
```
  mysql>grant all privileges on *.* to 'yaoyue'@'176.23.4.102' identified by '131227' with grant option;
  mysql>flush privileges;
  mysql> select * from mysql.user\G;

*************************** 10. row ***************************
                  Host: 176.23.4.102
                  User: yaoyue

mysql -uyaoyue -p   ##不可以登录
mysql -uyaoyue -h176.23.4.102 -p  ##可以登录
```
#### 3、添加用户duty,对db2库中所有表有所有权限
```
  mysql>grant all privileges on db2.* to 'duty'@'%' identified by '123' with grant option;
  mysql>flush privileges;
  mysql> select * from mysql.user\G;

  *************************** 5. row ***************************
                  Host: %
                  User: duty
终端输入mysql -uduty  -p123
查看用户select * from mysql.user\G;  host显示%；

可以查看db2库中的所有表：show databases;

mysql -uduty -p
```
**示例二**

test_utf8是在修改配置文件后，在创建表时也没有添加编码方式utf8的数据库结构
```
mysql> show create database test_utf8;
+-----------+--------------------------------------------------------------------+
| Database  | Create Database                                                    |
+-----------+--------------------------------------------------------------------+
| test_utf8 | CREATE DATABASE `test_utf8` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+-----------+--------------------------------------------------------------------+
1 row in set (0.00 sec)
```
db2是在没有修改配置文件，在创建表时也没有添加编码方式utf8的数据库结构
```
mysql> show create database db2;
+----------+----------------------------------------------------------------+
| Database | Create Database                                                |
+----------+----------------------------------------------------------------+
| db2      | CREATE DATABASE `db2` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+----------+----------------------------------------------------------------+
1 row in set (0.00 sec)

```

## **==事务和事务回滚==**

### **事务定义**

```mysql
 一件事从开始发生到结束的过程
```

### **作用**

```mysql
确保数据的一致性、准确性、有效性
```

### **事务操作**

1. 开启事务
   mysql>begin; # 方法1
   mysql>start transaction; # 方法2
2. 开始执行事务中的1条或者n条SQL命令
3. 终止事务
   mysql>commit; # 事务中SQL命令都执行成功,提交到数据库,结束!
   mysql>rollback; # 有SQL命令执行失败,回滚到初始状态,结束!

**模拟示例**

*创建表*
```mysql
 create table bank(
   name varchar(20),
   money decimal(20,2)
   )charset=utf8;

 insert into bank values
 ('vip1',20000),
 ('vip2',2000);
 ```
*rollback示例*
```
  begin;

 update bank set money=money-3000
  where name='vip1';

   select * from bank:
  +------+----------+
| name | money    |
+------+----------+
| vip1 | 17000.00 |
| vip2 |  2000.00 |
+------+----------+

work用户
因为没有提交，所以另一个用户的数据并未改变
   select * from bank:
  +------+----------+
| name | money    |
+------+----------+
| vip1 | 20000.00 |
| vip2 |  2000.00 |
+------+----------+

root用户
输入rollback后，root用户的数据恢复初始状态，数据更新失败，前提是要是‘事物’；

rollback

select * from bank:
  +------+----------+
| name | money    |
+------+----------+
| vip1 | 20000.00 |
| vip2 |  2000.00 |
+------+----------+

```
*commit示例*
```
root 用户

  begin;

 update bank set money=money-3000
  where name='vip2';

  commit;

 select * from bank:

+------+----------+
| name | money    |
+------+----------+
| vip1 | 20000.00 |
| vip2 |  5000.00 |
+------+----------+


work用户
select * from bank;
    
+------+----------+
| name | money    |
+------+----------+
| vip1 | 20000.00 |
| vip2 |  5000.00 |
+------+----------+

```
*在pycharm中的pymysql逻辑编写过程中大量使用*
```
try:
   转账1
   转账2
except:
   db.rollback()
db.commit()
```

## **==事务四大特性（ACID）==**

- **1、原子性（atomicity）**
注重结果
```
一个事务必须视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作
```

- **2、一致性（consistency）**
每个过程的状态。开始到结束中间有很多状态。
```
数据库总是从一个一致性的状态转换到另一个一致性的状态
```

- **3、隔离性（isolation）**

```
一个事务所做的修改在最终提交以前，对其他事务是不可见的
```

- **4、持久性（durability）**

```
一旦事务提交，则其所做的修改就会永久保存到数据库中。此时即使系统崩溃，修改的数据也不会丢失
```

**注意**

```mysql
1、事务只针对于表记录操作(增删改)有效,对于库和表的操作无效
2、事务一旦提交结束，对数据库中数据的更改是永久性的
```

## **E-R模型(Entry-Relationship)**

**定义**		

```mysql
E-R模型即 实体-关系 数据模型,用于数据库设计
用简单的图(E-R图)反映了现实世界中存在的事物或数据以及他们之间的关系
```

**实体、属性、关系**

- 实体

```mysql
1、描述客观事物的概念
2、表示方法 ：矩形框
3、示例 ：一个人、一本书、一杯咖啡、一个学生
```

- 属性

```mysql
1、实体具有的某种特性
2、表示方法 ：椭圆形
3、示例
   学生属性 ：学号、姓名、年龄、性别、专业 ... 
   感受属性 ：悲伤、喜悦、刺激、愤怒 ...
```

- ==关系（重要）==

```mysql
1、实体之间的联系
2、一对一关联(1:1) ：老公对老婆
   A中的一个实体,B中只能有一个实体与其发生关联
   B中的一个实体,A中只能有一个实体与其发生关联
3、一对多关联(1:n) ：父亲对孩子
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中只能有一个与其发生关联
4、多对多关联(m:n) ：兄弟姐妹对兄弟姐妹、学生对课程
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中有多个实体与其发生关联
```

**ER图的绘制**

矩形框代表实体,菱形框代表关系,椭圆形代表属性

- 课堂示例（老师研究课题）

```mysql
1、实体 ：教师、课题
2、属性
   教师 ：教师代码、姓名、职称
   课题 ：课题号、课题名
3、关系
   多对多（m:n)
   # 一个老师可以选择多个课题，一个课题也可以被多个老师选
```

- 练习

设计一个学生选课系统的E-R图

```mysql
1、实体：学生、课程、老师
2、属性
3、关系
   学生 选择 课程 (m:n)
   课程 任课 老师 (1:n)
```

==**关系映射实现（重要）**==

```mysql
1:1实现 --> 主外键关联,外键字段添加唯一索引
  表t1 : id int primary key,
          1
  表t2 : t2_id int unique,
         foreign key(t2_id) references t1(id)
          1
1:n实现 --> 主外键关联
  表t1 : id int primary key,
         1
  表t2 : t2_id int,
         foreign key(t2_id) references t1(id)
         1
         1        
m:n实现(借助中间表):
   t1 : t1_id 
   t2 : t2_id 
```
**==多对多实现==**

- 老师研究课题       *该表的数据都在db3库中*
```
表1、老师表 
表2、课题表
问题？如何实现老师和课程之间的多对多映射关系？
中间表：middle
```
导入数据
```
use db3;

source /home/tarena/1905/month03/code/code2/day03/mysql_day03/relation.sql

create table middle(
   id int primary key,
   tid int,cid int,
   foreign key(tid) references teacher(id),
   foreign key(cid) references course(id)
   )charset=utf8;

创建多对多的表
 insert into middle values (1,1,1),(2,1,2),(3,2,1),(4,2,3),(5,2,2);

```

- 后续

```mysql
1、每个老师都在研究什么课题？
select teacher.tname,course.cname from teacher inner join middle on teacher.id=middle.tid inner join course on middle.cid=course.id;
2、郭小闹在研究什么课题？
select teacher.tname,course.cname from teacher inner join middle on teacher.id=middle.tid inner join course on middle.cid=course.id where tname='郭小闹';
```

## **==MySQL调优==**

**存储引擎优化**

```mysql
1、读操作多：MyISAM
2、写操作多：InnoDB
```

**索引优化**

```
在 select、where、order by 常涉及到的字段建立索引
```

**SQL语句优化**

```mysql
1、单条查询最后添加 LIMIT 1，停止全表扫描
2、where子句中不使用 != ,否则放弃索引全表扫描
3、尽量避免 NULL 值判断,否则放弃索引全表扫描
   优化前：select number from t1 where number is null;
   优化后：select number from t1 where number=0;
   # 在number列上设置默认值0,确保number列无NULL值
4、尽量避免 or 连接条件,否则放弃索引全表扫描
   优化前：select id from t1 where id=10 or id=20;
   优化后： select id from t1 where id=10 union all 
           select id from t1 where id=20;
5、模糊查询尽量避免使用前置 % ,否则全表扫描
   select name from t1 where name like "c%";
6、尽量避免使用 in 和 not in,否则全表扫描
   优化前：select id from t1 where id in(1,2,3,4);
   优化后：select id from t1 where id between 1 and 4;
7、尽量避免使用 select * ...;用具体字段代替 * ,不要返回用不到的任何字段
```



**作业讲解**

有一张文章评论表comment如下

| **comment_id** | **article_id** | **user_id** | **date**            |
| -------------- | -------------- | ----------- | ------------------- |
| 1              | 10000          | 10000       | 2018-01-30 09:00:00 |
| 2              | 10001          | 10001       | ... ...             |
| 3              | 10002          | 10000       | ... ...             |
| 4              | 10003          | 10015       | ... ...             |
| 5              | 10004          | 10006       | ... ...             |
| 6              | 10025          | 10006       | ... ...             |
| 7              | 10009          | 10000       | ... ...             |

以上是一个应用的comment表格的一部分，请使用SQL语句找出在本站发表的所有评论数量最多的10位用户及评论数，并按评论数从高到低排序

备注：comment_id为评论id

​            article_id为被评论文章的id

​            user_id 指用户id

```
select use_id ,count(user_id) from comment
group by user_id
order by count(user_id) desc
limit 10;
```

2、把 /etc/passwd 文件的内容导入到数据库的表中

```mysql
tarena:x:1000:1000:tarena,,,:/home/tarena:/bin/bash
1、拷贝文件
   sudo cp /etc/passwd /var/lib/mysql-files
2、建表
  create table user(
  username varchar(20),
  password char(1),
  uid int,
  gid int,
  comment varchar(50),
  homedir varchar(100),
  shell varchar(50)
  )charset=utf8;
3、导入
  load data infile '/var/lib/mysql-files/passwd'
  into table user
  fields terminated by ':'
  lines terminated by '\n';
```

**3、外键及查询题目**

综述：两张表，一张顾客信息表customers，一张订单表orders

表1：顾客信息表，完成后插入3条表记录

```
c_id 类型为整型，设置为主键，并设置为自增长属性
c_name 字符类型，变长，宽度为20
c_age 微小整型，取值范围为0~255(无符号)
c_sex 枚举类型，要求只能在('M','F')中选择一个值
c_city 字符类型，变长，宽度为20
c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
```

```mysql
create table customers(
c_id int primary key auto_increment,
c_name varchar(20),
c_age tinyint unsigned,
c_sex enum('M','F'),
c_city varchar(20),
c_salary decimal(12,2)
)charset=utf8;
insert into customers values(1,'Tom',25,'M','上海',10000),(2,'Lucy',23,'F','广州',12000),(3,'Jim',22,'M','北京',11000);
```

表2：顾客订单表（在表中插入5条记录）

```
o_id 整型
o_name 字符类型，变长，宽度为30
o_price 浮点类型，整数最大为10位，小数部分为2位
设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(3,"mate9",3688),(2,"iwatch",2222),(2,"r11",4400);
```

```mysql
create table orders(
o_id int,
o_name varchar(30),
o_price decimal(12,2),
foreign key(o_id) references customers(c_id) on delete cascade on update cascade
)charset=utf8;
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(2,"iwatch",2222),(2,"r11",4400);
```

增删改查题

```mysql
1、返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录

2、把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
  
3、把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
  
4、选择工资c_salary最少的顾客的信息
  
5、找到工资大于5000的顾客都买过哪些产品的记录明细	
  
6、删除外键限制
 
7、删除customers主键限制
 
8、增加customers主键限制c_id
  
```

# 补充
## 1）管道查询
```
root@tarena:/var/lib/mysql/country# ls |grep 'sanguo'
tarena@tarena:~$ ps aux|grep 'mysqld' 
```
匹配字符'sanguo'查找显示

## 2）查看错误日志
```
数据库出错了，在error中查看日志
log_error = /var/log/mysql/error.log

打开方式
tarena@tarena:~$ cd /var/log/mysql
tarena@tarena:/var/log/mysql$ ls
error.log       error.log.2.gz  error.log.4.gz  error.log.6.gz
error.log.1.gz  error.log.3.gz  error.log.5.gz  error.log.7.gz
```

## 3） 查看系统日志
```
tarena@tarena:~$  cd /var/log
- 方法一：
tarena@tarena:/var/log$ vim /var/log/syslog
/log回车
 n是下一个，N 上一个
/MySQL 
- 方法二：
或者cat /var/log/syslog |grep 'MySQL '|more +
```

## 4）vim使用
   1. vi打不开的时候，可以使用vim
   2. vim修改时要点击i进入插入状态，
   3. 方向键：k是上移，j是下移,h是左移，l右移；
   4. set number 添加行号
   5. o从光标当前行 换行，并进入插入模式
   6. 插入模式后摁esc键切回阅读模式，
   7. 输入内件指定：w保存 q退出
   8. 3dd删除指定行数内容，3为指定行
   9. u撤销
   10. 在只读状态时末尾输入'\log'搜索含有log的字段。n是下一个，N是上一个。
   11. vim严格区分大小写
        
## 5）ifconfig查看网址（IP）
内网网址
```
enp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 176.23.4.102  netmask 255.255.255.0  broadcast 176.23.4.255
        inet6 fe80::be50:e020:e3d8:30a9  prefixlen 64  scopeid 0x20<link>
        ether fc:aa:14:eb:a5:58  txqueuelen 1000  (以太网)
        RX packets 4116  bytes 4459337 (4.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2287  bytes 256541 (256.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
本地网址
```
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (本地环回)
        RX packets 514  bytes 521475 (521.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 514  bytes 521475 (521.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## 6）查看进程
```
查看当前进程
tarena@tarena:~$ ps aux
查看当前进程在哪些用户下进行
tarena@tarena:~$ ps aux|grep 'mysqld'
mysql     1081  0.0  4.7 1417112 189108 ?      Sl   08:13   0:02 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid
tarena   14473  0.0  0.0  21532  1004 pts/2    S+   09:35   0:00 grep --color=auto mysqld
tarena@tarena:~$ 
查看当前进程进行的总个数
tarena@tarena:~$ ps aux|grep 'mysqld'|wc -l
2
```

## 7）哈希算法
```
哈希算法就是散列函数，散列值（在下载环境中大量使用）

eg: '12345678'--->'ABCDE'（MD5）

特点：
1. 输入为不定长的值，输出一定为定长值
2.不可逆，不可以由定长值转换为不定长值  '12345678'<-!=--'ABCDE'
3.雪崩效应，修改不定长字符中的任意一个，输出的结果一定大不相同

密码（散列，散列值）
用char类型的字段，因为肯定会对密码进行哈希算法，根据散列的三大特点之一，因为输出为定长，所以char更好。varchar也可以存储密码，但是由于varchar有扩展字段，去存储一个输入字符的实际长度，由于已经定长了，就会浪费磁盘空间。
```

## 8）配置文件etc
```
etc：该目录一般会存当前系统（ubantu)的所有安装的软件的配置文件，前提是有超级用户root权限才能打开，在修改配置文件之前最好备份copy一份。
eg:mysql的配置文件
cd /etc/mysql/mysql.conf.d
```