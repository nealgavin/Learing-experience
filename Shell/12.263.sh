#!/bin/bash
var1=1
while [ $var1 -lt 10 ]
do
	if [ $var1 -eq 5 ]
	then 
		break
	fi
	echo "iteration: $var1"
	var1=$[ $var1+1 ]
done

IFS.OLD=$IFS
IFS=$'\n'
for entry in `cat /etc/passwd`
do
	echo "Values in $entry -"
	IFS=:
	for value in $entry
	do
		echo "	$value"
	done
done
