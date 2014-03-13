#!/bin/bash
#testing string
testuser=gavin
if [ $USER = $testuser ]
then
	echo welcome $testuser
fi
val1=baseball
val2="hockey"
if [ $val1 \> $val2 ]
then
	echo $val1 is biger than $val2
else
	echo $val1 is lower than $val2
fi
