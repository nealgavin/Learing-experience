#!/bin/bash
#testing the else section
echo enter the name of user
read testuser
if grep $testuser /etc/passwd
then
	echo The file for user $testuser are:
	ls -a /home/$testuser/.b*
else
	echo "The user name $testuser does not exits on this System"
fi
