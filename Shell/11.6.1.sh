#!/bin/bash
# testing for (())
val1=10
if (( $val1 ** 2 > 90 ))
then
	(( val2=$val1 ** 2 ))
	echo  "the square of $val1 is $val2"
fi

