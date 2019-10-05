#!/bin/bash

sumn(){
	echo $[n1+n2]
}

sunb(){
	echo $[n1-n2]
}

read -p "First:" n1
read -p "Second:" n2
read -p "opration(+|-):" op

case $op in
"+")
	sumn
	;;
"-")
	sunb
	;;
*)
	echo "Invaid"
	;;
esac
