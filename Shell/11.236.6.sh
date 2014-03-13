#!/bin/bash
#checking if a file is writeaable
logfile=$HOME/code/testlog
if [ -f $logfile ]
then
	echo $logfile is exit
else
	touch $logfile
fi
chmod u-w $logfile
now=`date +%Y-%m-%d-%H:%M`

if [ -w $logfile ]
then
	echo "The program ran at :$now" > $logfile
	echo "the first success!"
else
	echo "failed!"
fi
chmod u+w $logfile


if [ -w $logfile ]
then
	echo "The program ran at :$now" >> $logfile
	echo "the first success!"
else
	echo "failed!"
fi

