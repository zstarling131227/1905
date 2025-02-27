# MySQL高级-Day01回顾

- **SQL查询总结**

```mysql
    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
```

- **聚合函数（铁三角之一）**

avg(...) sum(...) max(...) min(...) 
count(字段名)  # 空值NULL不会被统计

- **group by（铁三角之二）**

给查询结果进行分组
如果select之后的字段名和group by之后的字段不一致,则必须对该字段进行聚合处理(聚合函数)

- **having语句（铁三角之三）**

对查询的结果进行进一步筛选
**注意**
1、having语句通常和group by语句联合使用,过滤由group by语句返回的记录集
2、where只能操作表中实际存在字段,having可操作由聚合函数生成的显示列

- **distinct** 

select distinct 字段1,字段2 from 表名;

- **查询时做数学运算**

select 字段1*2,字段2+5 from 表名;

update 表名 set attack=attack*2 where 条件;

- **索引(BTree)**

优点 ：加快数据检索速度
缺点 ：占用物理存储空间,需动态维护,占用系统资源
SQL命令运行时间监测

​		mysql>show variables like '%pro%';

​		1、开启 ：mysql> set profiling=1;
​		2、查看 ：mysql> show profiles;
​		3、关闭 ：mysql> set profiling=0;

- **普通(MUL)、唯一(UNI,字段值不能重复,可为NULL)**

  **创建**
  		index(字段名),index(字段名)
  		unique(字段名),unique(字段名)
  		create [unique] index 索引名 on 表名(字段名);

  **查看**
  		desc 表名;
  		show index from 表名\G;  
  			Non_Unique:1 :index
  			Non_Unique:0 :unique

  **删除**
  		drop index 索引名 on 表名; (只能一个一个删)

# MySQL高级-Day02笔记

## **外键（foreign key）**

- **定义**

  让当前表字段的值在另一个表的范围内选择

- **语法**

  ```mysql
  foreign key(参考字段名)
  references 主表(被参考字段名)
  on delete 级联动作
  on update 级联动作
  ```

- **使用规则**

1. 主表、从表字段数据类型要一致
2. 主表被参考字段 ：KEY的一种，一般为主键

- **示例**
*-该表在数据库db2中*
*-对从表做操作时主表要有数据*

表1、缴费信息表(财务)

```mysql
id   姓名     班级     缴费金额
1   唐伯虎   AID1903     300
2   点秋香   AID1903     300
3   祝枝山   AID1903     300
create database db2 charset utf8;
use db2;
create table master(
  id int primary key auto_increment,
  name varchar(20),
  class varchar(30),
  money decimal(6,2)
  )charset=utf8;

 insert into master (name,class,money) values('唐伯虎','AID1905',300);

insert into master (name,class,money) values('点秋香','AID1905',300),('祝枝山','AID1905',300);

insert into master (name,class,money) values('腊梅','AID1905',300),('秋菊','AID1905',300);

```

表2、学生信息表(班主任) -- 做外键关联

```mysql
stu_id   姓名   缴费金额
  1     唐伯虎    300
  2     点秋香    300

create table slave(
  stu_id int,
  name varchar(20),
  money decimal(6,2),
  foreign key(stu_id)
  references master(id) 
  on delete cascade
  on update cascade
  )charset=utf8;

insert into slave values(1,'唐伯虎',300),(2,'点秋香',300);
insert into slave values(3,'腊梅',300),(4,'秋菊',300);

 insert into slave values(6,'xixi',300);
```
*报错：*
在从表中插入主表master中没有的数据时，会报错
```
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`stu`.`slave`, CONSTRAINT `slave_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `master` (`id`) ON DELETE CASCADE ON UPDATE CASCADE)
```
表结构：有外键的会多出  《CONSTRAINT `slave_ibfk_1`……》
```
mysql> show create table slave\G;
*************************** 1. row ***************************
       Table: slave
Create Table: CREATE TABLE `slave` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` decimal(6,2) DEFAULT NULL,
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `slave_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `master` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
```

- **删除外键**

```mysql
alter table 表名 drop foreign key 外键名;
​外键名 ：show create table 表名;

create table slave1(
  stu_id int ,
  name varchar(20),
  money decimal(6,2),
  foreign key(stu_id) references master(id)
  on delete cascade
  on update cascade)
  charset=utf8;

insert into slave1 values
(1,'唐伯虎',300),
(2,'点秋香',300),
(3,'腊梅',300),
(4,'秋菊',300);

stu_id 是字段名，关键字是slave1_ibfk_1；
alter table slave1 drop foreign key(stu_id);##报错
alter table slave1 drop foreign key slave1_ibfk_1;

show create table slave1\G;
*************************** 1. row ***************************
       Table: slave1
Create Table: CREATE TABLE `slave1` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` decimal(6,2) DEFAULT NULL,
  KEY `stu_id` (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
```
- **级联动作**
*多从表关联同一个主表的时候，从表中的数据不可以重复，且都要在主表中存在，否则会报错。*

#### 1)cascade ​数据级联删除、更新(参考字段)
```mysql
create table slave2(
  stu_id int ,
  name varchar(20),
  money decimal(6,2),
  foreign key(stu_id) references master(id)
  on delete cascade
  on update cascade)
  charset=utf8;

 insert into slave2 values(1,'唐伯虎',300),(2,'点秋香',300),(3,'祝枝山',300);
 insert into slave2 values(1,'腊梅',300),(2,'秋菊',300);
```
**主从表的操作一致。** *也就是说，主表master删除id=1的数据时，从表slave2的stu_id=1数据自动同步删除。主表master更新id=5的数据时，从表slave2的stu_id=5数据自动同步更新。如果从表中没有主表中的数据，则只对主表进行操作。*
```
 delete from master where id=1;
 update master set id=10 where id=4;
```
#### 2)restrict(默认)  ​从表有相关联记录,不允许主表操作
```mysql
 create table slave3(
   stu_id int,
   name varchar(20),
   money decimal(6,2),
   foreign key(stu_id) 
   references master(id)
   )charset=utf8;
```
**数据插入注意**
```
##插入主表中有的数据，外键（id)数据要相同，否则会报错
   insert into slave3 values(2,'点秋香',300);
##主表中没有(1,'唐伯虎',300)故报错
insert into slave3 values(1,'唐伯虎',300),(2,'点秋香',300);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`stu`.`slave3`, CONSTRAINT `slave3_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `master` (`id`))
```
对主表不能做任何更新或删除数据，只能对主表做插入操作
```
mysql> delete from master where id=2;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`test`.`slave3`, CONSTRAINT `slave3_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `master` (`id`))
```
若是想对主表做删除等操作，需要先从从表中删除数据,再对主表进行操作
```
mysql> delete from slave3 where stu_id=2;
mysql> delete from master where id=2;
```

#### 3) set null 主表删除、更新,从表相关联记录字段值为NULL
```mysql
create table slave4(
  stu_id int,
  name varchar(20),
  money decimal(6,2),
  foreign key(stu_id) references master(id) 
  on delete set null on update set null)
  charset=utf8;

insert into slave4 values
(1,'唐伯虎',300),
(2,'点秋香',300),
(3,'祝枝山',300);

delete from master where id=2;
```
**主从表的操作不一致。** *也就是说，主表master删除id=2的数据时，从表slave4的stu_id=2数据不会自动同步删除。主表master中id=2的数据全部删除，从表slave4的stu_id=2变为stu_id=NULL。如果从表中没有主表中的数据，则只对主表进行操作。*
```
mysql> select * from slave4;
+--------+-----------+--------+
| stu_id | name      | money  |
+--------+-----------+--------+
|      1 | 唐伯虎    | 300.00 |
|   NULL | 点秋香    | 300.00 |
|      3 | 祝枝山    | 300.00 |
+--------+-----------+--------+
3 rows in set (0.00 sec)
```
- **已有表添加外键**

```mysql
alter table 表名 add foreign key(参考字段) references 主表(被参考字段) on delete 级联动作 on update 级联动作
```

## 嵌套查询(子查询)

定义

把内层的查询结果作为外层的查询条件

语法格式

```mysql
select ... from 表名 where 条件(select ....);
```

示例

```mysql
1、把攻击值小于平均攻击值的英雄名字和攻击值显示出来
  select  name,attack from sanguo where attack<(select avg(attack) from sanguo);

2、找出每个国家攻击力最高的英雄的名字和攻击值(子查询)
  select  name,attack from sanguo where (country,attack) in (select country,max(attack) from sanguo group by country);
```

## **多表查询**

**sql脚本资料：join_query.sql**

***该数据表在country数据库下***
```mysql
mysql -uroot -p123456
此时的文件在根目录下
mysql>source /home/tarena/join_query.sql
##指文件所在路径
source /home/tarena/1905/month03/code/code2/day02/mysql_day02/join_query.sql
```
*执行后country库中多出下列3个表*
```
+----------------+
| city           |
| county         |
| province       |
+----------------+
```
**windows系统下的插入：直接创建表再粘贴数据**
```mysql
create database if not exists db1 character set utf8;
use db1;

create table if not exists province(
id int primary key auto_increment,
pid int,
pname varchar(15)
)default charset=utf8;

insert into province values
(1, 130000, '河北省'),
(2, 140000, '陕西省'),
(3, 150000, '四川省'),
(4, 160000, '广东省'),
(5, 170000, '山东省'),
(6, 180000, '湖北省'),
(7, 190000, '河南省'),
(8, 200000, '海南省'),
(9, 200001, '云南省'),
(10,200002,'山西省');

create table if not exists city(
id int primary key auto_increment,
cid int,
cname varchar(15),
cp_id int
)default charset=utf8;

insert into city values
(1, 131100, '石家庄市', 130000),
(2, 131101, '沧州市', 130000),
(3, 131102, '廊坊市', 130000),
(4, 131103, '西安市', 140000),
(5, 131104, '成都市', 150000),
(6, 131105, '重庆市', 150000),
(7, 131106, '广州市', 160000),
(8, 131107, '济南市', 170000),
(9, 131108, '武汉市', 180000),
(10,131109, '郑州市', 190000),
(11,131110, '北京市', 320000),
(12,131111, '天津市', 320000),
(13,131112, '上海市', 320000),
(14,131113, '哈尔滨', 320001),
(15,131114, '雄安新区', 320002);

create table if not exists county(
id int primary key auto_increment,
coid int,
coname varchar(15),
copid int
)default charset=utf8;

insert into county values
(1, 132100, '正定县', 131100),
(2, 132102, '浦东新区', 131112),
(3, 132103, '武昌区', 131108),
(4, 132104, '哈哈', 131115),
(5, 132105, '安新县', 131114),
(6, 132106, '容城县', 131114),
(7, 132107, '雄县', 131114),
(8, 132108, '嘎嘎', 131115);
```

- **笛卡尔积**
*ttl，tt2，tt3都在数据库country下*
```mysql
select 字段名列表 from 表名列表; 

create table ttl(tt1name varchar(20));
create table tt2(tt2name varchar(20));
create table tt3(tt3name varchar(20));

insert into ttl values('A1'),('A2'),('A3');
insert into tt2 values('B1'),('B2'),('B3');
insert into tt3 values('C1'),('C2');

select * from ttl,tt2;
select * from tt2,tt3;

```
- **多表查询**

```mysql
select 字段名列表 from 表名列表 where 条件;
```

- **示例**

```mysql
1、显示省和市的详细信息
   河北省  石家庄市
   河北省  廊坊市
   湖北省  武汉市

  select province.pname, city.cname from province,city
  where province.pid=city.cp_id;

2、显示 省 市 县 详细信息
  select province.pname, city.cname,county.coname    
  from province,city,county
  where province.pid=city.cp_id and city.cid=county.copid;
```

## 连接查询

- **内连接（结果同多表查询，显示匹配到的记录）**

````mysql
select 字段名 from  表1 inner join 表2 on 条件 inner join 表3 on 条件;
eg1 : 显示省市详细信息
  select province.pname, city.cname    from province inner join city     on  province.pid=city.cp_id;

eg2 : 显示 省 市 县 详细信息
  select province.pname, city.cname,county.coname  
  from province 
  inner join city  join county    
  on province.pid=city.cp_id and city.cid=county.copid;

  select province.pname, city.cname,county.coname
  from province
  inner join city 
  on province.pid=city.cp_id
  inner  join county
   on city.cid=county.copid;

````

- **左外连接**

以 左表 为主显示查询结果

```mysql
select 字段名 from 表1 left join 表2 on 条件 left join 表3 on 条件;
eg1 : 显示 省 市 详细信息（要求省全部显示）
 
 select province.pname, city.cname,county.coname
 from province
 left  join city
 on province.pid=city.cp_id
 left  join county 
 on city.cid=county.copid;

```

- **右外连接**

用法同左连接,以右表为主显示查询结果

```mysql
select 字段名 from 表1 right join 表2 on 条件 right join 表3 on 条件;

eg1 : 显示 省 市 详细信息（要求县全部显示）
select province.pname, city.cname,county.coname
from province
right  join city
on province.pid=city.cp_id
right  join county
on city.cid=county.copid;
```

## **数据导入**

==掌握大体步骤==

==source 文件名.sql==

**作用**

把文件系统的内容导入到数据库中
**语法（方式一）**

load data infile "文件名"
into table 表名
fields terminated by "分隔符"
lines terminated by "\n"
**示例**
scoretable.csv文件导入到数据库db2的表
*该表在数据库代表db2中*

**1、将scoretable.csv放到数据库搜索路径中**
```mysql 
  查询位置
  mysql>show variables like 'secure_file_priv';
  存入到指定位置：/var/lib/mysql-files/
  从主目录下复制到指定存入位置
   Linux: sudo cp /home/tarena/scoreTable.csv /var/lib/mysql-files/
  从自己目录下复制到指定存入位置
    Linux: sudo cp /home/tarena/1905/month03/code/code2/day02/mysql_day02/scoreTable.csv /var/lib/mysql-files
```
终端下的操作
```
tarena@tarena:~$ sudo cp /home/tarena/1905/month03/code/code2/day02/mysql_day02/scoreTable.csv /var/lib/mysql-files
tarena@tarena:~$ sudo su
root@tarena:/home/tarena# cd /var/lib/mysql-files/
root@tarena:/var/lib/mysql-files# ls
scoreTable.csv
root@tarena:/var/lib/mysql-files# 

此时是没有修改权限的
root@tarena:/var/lib/mysql-files# ll |grep 'sc'
-rw-rw-rw-  1 root  root  1719 8月  10 18:01 scoreTable.csv

##修改文件权限
root@tarena:/var/lib/mysql-files# chmod 666 scoreTable.csv
root@tarena:/var/lib/mysql-files# ll |grep 'sc'
-rw-rw-rw-  1 root  root  1719 8月  10 18:01 scoreTable.csv
```
### 补充
1)管道符操作：ll列表形式查看文件列表，grep 管道模糊匹配查询文件 'sc'为查询字符

```
root@tarena:/var/lib/mysql-files# ll |grep 'sc'
-rw-rw-rw-  1 root  root  1719 8月  10 18:01 
```
2)查看mysql进程：ps aux|grep "mysql"

```
tarena@tarena:~$ ps aux|grep "mysql"
mysql     1067  1.4  4.5 2072896 181744 ?      Sl   10:06   6:50 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid
tarena    7859  0.0  0.1  43216  4204 pts/0    S+   10:54   0:06 mysql -uroot -px xxxx
tarena   14519  0.0  0.0  21532   996 pts/2    S+   18:08   0:00 grep --color=auto mysql

```
3)修改文件权限

```
root@tarena:/var/lib/mysql-files# chmod 666 scoreTable.csv
```
4)目前系统下的所有ubantu用户和相应的密码，和相应的家在哪里。退出时输入：':q'回车

```
tarena@tarena:~$ vim /etc/passwd

tarena:x:1000:1000:tarena,,,:/home/tarena:/bin/bash
x是密码占位符；':'是分隔符；'/home/tarena'是家的位置；'/bin/bash'是登录权限
```
**2、在数据库中创建对应的表**
*该scoretab表在数据库db2中由于创建数据库时没有设置字符编码为charset=utf8,name一列出现乱码*
*不乱码的scoretab表在数据库db22中*

```
  create table scoretab(
  rank int,
  name varchar(20),
  score float(5,2),
  phone char(11),
  class char(7)
  )charset=utf8;
```
**3、执行数据导入语句**
```
load data infile '/var/lib/mysql-files/scoreTable.csv'
into table scoretab
fields terminated by ','
lines terminated by '\n';
```
**4、练习**
```
  添加id字段,要求主键自增长,显示宽度为3,位数不够用0填充
  alter table scoretab add id int(3) zerofill primary key auto_increment first;
```

**语法（方式二）**

source 文件名.sql

## **数据导出**

**作用**

将数据库中表的记录保存到系统文件里

**语法格式**
***文件名一般指带有路径的文件名***

select ... from 表名
into outfile "文件名"   
fields terminated by "分隔符"
lines terminated by "分隔符";

**练习**

1、把sanguo表中英雄的姓名、攻击值和国家三个字段导出来,放到 sanguo.csv中

先导出到指定位置，
```mysql
select name,attack,country  from sanguo
into outfile "/var/lib/mysql-files/sanguo.csv"
fields terminated by ","
lines terminated by "\n";
```
再复制或移动到自己所定位置
```
root@tarena:/var/lib/mysql-files# ls
sanguo.csv  scoreTable.csv
root@tarena:/var/lib/mysql-files# cp sanguo.csv /home/tarena/1905/month03/code/code2/day02/
root@tarena:/var/lib/mysql-files# mv sanguo.csv /home/tarena/1905/month03/code/code2/day02/
root@tarena:/var/lib/mysql-files# ls
scoreTable.csv
```
2、将mysql库下的user表中的 user、host两个字段的值导出到 user2.txt，将其存放在数据库目录下

 ```mysql

use mysql

select user,host  from user
into outfile "/var/lib/mysql-files/user2.txt"
fields terminated by "*"
lines terminated by "\n";

root@tarena:/var/lib/mysql-files# ls
scoreTable.csv  user2.txt
root@tarena:/var/lib/mysql-files# mv user2.txt /home/tarena/1905/month03/code/code2/day02/
root@tarena:/var/lib/mysql-files# ls
scoreTable.csv
 ```
*不可以直接从mysql中直接导入到自己指定位置，否则会报错*
```
select user,host  from user
into outfile "/home/tarena/user2.txt"
fields terminated by "*"
lines terminated by "\n";

出现下面报错是路径问题
ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
```

**注意**

```
1、导出的内容由SQL查询语句决定
2、执行导出命令时路径必须指定在对应的数据库目录下(/var/lib/mysql-files/)
```

## **表的复制**

==1、表能根据实际需求复制数据==

==2、复制表时不会把KEY属性复制过来==

**语法**

```mysql
create table 表名 select 查询命令;
```

**练习**
*sanguo2,3,4表在country中*
```mysql
1、复制sanguo表的全部记录和字段,sanguo2
  create table sanguo2 select * from sanguo;
2、复制sanguo表的 id,name,country 三个字段的前3条记录,sanguo4
  create table sanguo4 select id,name,country from sanguo;
```

**注意**

复制表的时候不会把原有表的 KEY 属性复制过来

**复制表结构**
只复制结构，数据不复制
```
create table 表名 select 查询命令 where false;

create table sanguo3 select * from sanguo where false;
select * from sanguo3;
Empty set (0.00 sec)
```
## **锁（自动加锁和释放锁）**

==全程重点，理论和锁分类及特点==

**目的**

解决客户端并发访问的冲突问题

**锁类型分类**

```
读锁(共享锁)：select 加读锁之后别人不能更改表记录,但可以进行查询
写锁(互斥锁、排他锁)：加写锁之后别人不能查、不能改
```

**锁粒度分类**

表级锁 ：myisam
行级锁 ：innodb

# 今日作业

1、把 /etc/passwd 文件的内容导入到数据库的表中
*该passwd在数据库country中*
```
tarena:x:1000:1000:tarena,,,:/home/tarena:/bin/bash
```
终端操作
```
tarena@tarena:~$ cp /etc/passwd /home/tarena/
tarena@tarena:~$ sudo cp /home/tarena/passwd /var/lib/mysql-files/
[sudo] tarena 的密码： 
tarena@tarena:~$ sudo su
root@tarena:/home/tarena# cd /var/lib/mysql-files/
root@tarena:/var/lib/mysql-files# ls
passwd  scoreTable.csv
root@tarena:/var/lib/mysql-files# vim passwd
```
mysql操作
```
use country;

create table passwd(
  username varchar(20),
  passwd varchar(10),
  group1 int,
  group2 int,
  name1 varchar(50),
  home varchar(100),
  path varchar(50)
)charset=utf8;

load data infile '/var/lib/mysql-files/passwd'
into table passwd
fields terminated by ':'
lines terminated by '\n';
```

2、Day01的md文件中的外键及查询作业题





