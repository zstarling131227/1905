#!/bin/bash


# 2到254的数
for ip in {2..254}
do
	# /dev/null是黑洞，不想要的输出放在里面
	ping -c 2 172.40.91.$ip &> /dev/null
	#  $? # 判断上一条语句是否成功
	if [ $? -eq 0 ];then
		echo "172.40.91.$ip可用"
	else
		echo "172.40.91.$ip不可用"
	fi
done
