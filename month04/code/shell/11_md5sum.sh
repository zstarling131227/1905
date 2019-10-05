#!/bin/bash

for file in $(ls /etc/*.conf)
do
	echo $file
#	md5sum$file
	md5sum $file >>r1.txt
done
