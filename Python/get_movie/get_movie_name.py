#!/usr/bin/env python
# coding=utf-8
#########################################
	#> FmZ
import re
import urllib2
import BeautifulSoup
import string
from sgmllib import SGMLParser
import sys

NUM = 0         #全局 电影数量
m_type = u''    #电影类型
m_site = u'qq'  #电影网站

def gethtml(url):
    """获取网页的代码"""
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

url = 'http://v.qq.com/list/1_-1_-1_-1_2_0_0_20_0_-1_0.html'

def gettags(html):
    global m_type
    soup = BeautifulSoup(html)
    print soup
    tags_all = soup.find_all( 'ul', {'class':'clearfix_group','gname':'mi_type'} )
    re_tags = r'<a _hot=\"tag.sub\" class=\"_gtag_hotkey\" href=\"(.+?)\" title=\"(.+?)\" tvalue=\"(.+?)\">.+?</a>'
    print tags_all
    p = re.compile(re_tags,re.DOTALL)
    tags = p.findall(str(tags_all[0]))
    print tags

#print gethtml(url)
gettags(gethtml(url))
