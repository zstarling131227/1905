#!/bin/bash
  

cop=$RANDOM
#echo $c
c=$[RANDOM%10000]
while :
do 
	read -p "数字" you
	if [ $you -gt $cop ];then
		echo "大"
	elif [ $you -lt $cop ];then
		echo "小"
	else
		echo "正确"
		exit  # 退出终端
	fi
done
