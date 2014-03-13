#!/bin/bash
#look before you leap
if [ -d $HOME ]
then
	echo Your HOME directory exists
	cd $HOME
	ls -al
else
	echo Thereis a problem with your HOME directory
fi

