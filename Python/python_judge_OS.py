#!/usr/bin/env python
# coding=utf-8
#########################################
	#> File Name: python_judge_OS.py
	#> Author: nealgavin
	#> Mail: nealgavin@126.com 
	#> Created Time: Sat 24 May 2014 06:32:45 PM CST
#########################################

import platform

def TestPlatForm():
    print "--------------Operation System------------"

    print platform.architecture()
    print platform.platform()
    print platform.system()
    print platform.python_version()

def JudgeOS():
    TestPlatForm()
    sysstr = platform.system()
    if sysstr == "Windows":
        print ("Call Windows tasks")
    elif (sysstr == "Linux"):
        print ("Call Linux tasks")
    else:
        print ("Call other System")

JudgeOS()
