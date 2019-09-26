#!/bin/bash

# echo $1+$2
# echo `expr $1 + $2`

read -p 请输入姓名： name
echo "您输入的姓名是：$name"

read -t 3 -p 年龄： age
echo "年龄是：$age"

echo "$name的年龄是$age"
