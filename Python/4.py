#!/bin/
"""
def f(x,*fuck):
	print x
	print fuck
f(1)
f(1,2,3,4,5,6,7)
f(1,"34","456")
"""
l=range(1,10)
f=lambda x,y:x*y
print reduce(f,l)
