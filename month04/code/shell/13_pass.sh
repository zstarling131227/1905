#!/bin/bash

key="zxcvbnmasdfghjklpoiuytrewqQWERTYUIOPLKJHGFDSAZXCVBNM0123456789_"
length=${#key}
# 循坏8次
for i in {1..8}
do
	index=$[RANDOM%length]
	pass=$pass${key:$index:1}
done
echo $pass
