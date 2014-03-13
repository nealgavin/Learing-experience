#!/bin/bash
#tesing file is empty
pwfile=/etc/shadow
#is exit
if [ -f $pwfile ]
then
	ls -l $pwfile
	if [ -r $pwfile ]
	then
		tail $pwfile
	else
		echo "sorry,unable to read!"
	fi
else
	echo "sorry, the file $pwfile does not exist"
fi
