#!/bin/bash
#using numeric test comparisons
echo enter the  two number
read val1
read val2
if [ $val1 -gt 5 ]
then
	echo "the test value $val1 is greater than 5"
fi
echo the two num val1: $val1 val2:$val2
if [ $val1 -eq $val2 ]
then
	echo "the two value is eaual"
else
	echo "the values are different"
fi
