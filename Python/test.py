#!/usr/bin/env python
# coding=utf-8
#########################################
	#> File Name: test.py
	#> Author: nealgavin
	#> Mail: nealgavin@126.com 
	#> Created Time: Sat 24 May 2014 04:24:48 PM CST
#########################################
class superList(list):
    def __sub__(self,b):
        a = self[:]
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return superList(a)
out = superList([1,2,3]) - superList([3,4])
print out
print dir(list)
