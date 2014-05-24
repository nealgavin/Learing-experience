#!/usr/bin/env python
# coding=utf-8
#########################################
	#> File Name: rename.py
	#> Author: nealgavin
	#> Mail: nealgavin@126.com 
	#> Created Time: Sat 24 May 2014 04:56:03 PM CST
#########################################

import os

path = '/home/gavin/code/git/Learing-experience/linux/'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file)) == True:
        newname = file.replace(".my","")
        os.rename(os.path.join(path,file),os.path.join(path,newname))
        print (file)
