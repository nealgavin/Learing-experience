#!/bin/bash
fuck=$@
echo $fuck
for i in $fuck
do
	echo "haha:$i"
done
echo There is $# 个数
fac=1
echo $0
for (( num=1; num<$1; num++ )) 
do
	fac=$[ $fac * $num ]
done
echo The fac of $1 is $fac

