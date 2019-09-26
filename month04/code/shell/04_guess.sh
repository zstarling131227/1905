#!/bin/bash


cop=$RANDOM
read -p "数字" you
if [ $you -gt $cop ];then
	echo "大"
elif [ $you -lt $cop ];then
	echo "小"
else
	echo "正确"
fi

