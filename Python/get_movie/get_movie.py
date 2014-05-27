#!/usr/bin/env python
# coding=utf-8
#########################################
	#> File Name: get_movie.py
	#> Author: nealgavin
	#> Mail: nealgavin@126.com 
	#> Created Time: Sat 24 May 2014 09:03:58 PM CST
#########################################
#########################################
#can get the name and link of QQ Movie
#########################################
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


def out_Chinese(tags):
    for tag in tags:
        print str(tag)

def gettags(html):
    global m_type
    #print html
    soup = BeautifulSoup.BeautifulSoup(html)
    #print soup
    tags_all = soup.findAll( 'div',{ 'class':'grid_18' } )
    re_tags = r'<h6 class="scores">(.+?)</h6>'
    re.UNICODE
    p = re.compile(re_tags,re.DOTALL)
    tags = p.findall(str(tags_all[0]))
#    print tags_all
#    print "++"*300
    return tags

def buildMovieName(url):
    print '<html><meta charset="utf-8"><head>Tecent Movie</head><body>'
    out_Chinese(gettags(gethtml(url)))
    print '</body></html>'

def getMovieName(tags):
    tags = gettags(gethtml(tags))
    movieNames = []
    re_rules = r'<a href="(.+?)" title="(.+?)" target="(.*?)">'
    match = re.compile(re_rules)
    for tag in tags:
        name = match.findall(tag)[0]
        movieNames.append(name[1])#movie name
        movieNames.append(name[0])#movie link
    out_Chinese(movieNames)
    return movieNames
#print gethtml(url)
#buildMovieName(url)

url = raw_input("Input the link of QQ movie\n")
if url is None or len(url) == 0:
    url = 'http://v.qq.com/list/1_-1_-1_-1_2_0_0_20_0_-1_0.html'
print url
getMovieName(url)
