#!/usr/bin/env python
import urllib.request
webpage = raw_input("input the web  page")
fp = urllib.request.urlopen(webpage)
mybytes = fp.read()

mystr = mybytes.decode("utf-8")
print mystr
fp.close()
