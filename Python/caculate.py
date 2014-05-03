#!/usr/bin/python
#coding:utf-8

from __future__ import division
def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y
def operator(x,o,y):
	if o == "+":
		print add(x,y)
	elif o == "-":
		print sub(x,y)
	elif o == "*":
		print mul(x,y)
	elif o == "/":
		print div(x,y)
	else:
		pass
operator(3,'*',7)

