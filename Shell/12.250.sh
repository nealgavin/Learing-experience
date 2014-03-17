#!/bin/bash
file="11*"
IFS=$'\n'
for state in `cat $file`
do
	echo "key: $state"
done
