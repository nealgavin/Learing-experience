#!/bin/bash
#testing commands
echo "enter the user name"
read testuser
if grep $testuser /etc/passwd
then
	echo The bash files for user $testuser are:
	ls -a /home/$testuser/.b*
fi
