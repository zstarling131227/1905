#!/bin/bash

user="root"
passwd="123456"
dbname="mysql"
filename=$(date +%F)-mysql.sql

# 1.创建文件
# -d判断一个文件是不是目录
#! -d 表示目录不存在
if [ ! -d "/home/tarena" ];then
	mkdir -p /home/tarena/backup
fi
#备份
mysqldump -u$user -p$passwd $dbname > /home/tarena/$filename

