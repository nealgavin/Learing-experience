#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import re
import urllib2
from BeautifulSoup import BeautifulSoup
import string
from sgmllib import SGMLParser
import sys
 
 
NUM = 0         #全局变量,电影数量
m_type = u''    #全局变量,电影类型
m_site = u'qq'  #全局变量,电影网站
 
def gethtml(url):
    req = urllib2.Request(url) 
    response = urllib2.urlopen(req) 
    html = response.read()
    return html
 
def gettags(html):
    global m_type
    soup=BeautifulSoup(html)
    tags_all = soup.findAll('ul', {'class' : 'clearfix _group','gname':'mi_type'})
 
    re_tags = r'<a _hot=\"tag.sub\" class=\"_gtag _hotkey\" href=\"(.+?)\" title=\"(.+?)\" tvalue=\"(.+?)\">.+?</a>'
    p=re.compile(re_tags,re.DOTALL)
    tags = p.findall(str(tags_all[0]))
    tags_url = ""
    if tags:
        tags_url = {}
        for tag in tags:
            tag_url = tag[0].decode('utf-8')
            m_type = tag[1].decode('utf-8')
            tags_url[m_type] = tag_url
     
        for url in tags_url.items():
            maxpages = int(get_pages(str(url[1]).encode('utf-8')))
            m_type=url[0]
            for x in range(0,maxpages):
                m_url = str(url[1].replace('2_0_0_20_0_-1_0.html',''))
                movie_url = "%s2_0_%d_20_0_-1_0.html"%(m_url,x)
                print movie_url,m_type.encode('utf-8')
                movie_html = gethtml(movie_url)
                getmovielist(movie_html)
 
    else:
        print 'Not find'
    return tags_url
 
class ListName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_div=""
        self.name = []
    def start_div(self,attrs):
        for k,v in attrs:
            if k=="class" and v=="mod_pagenav":
                self.is_div=1
                return
    def end_div(self):
        self.is_div=""
    def handle_data(self,text):
        if self.is_div ==1:
            self.name.append(text)
 
 
def get_pages(tag_url):
 
    tag_html = gethtml(tag_url)
 
    listname=ListName()
    listname.feed(tag_html)
    newlist=[]
    for i in listname.name:
        if i!= '\n\t\t':
            newlist.append(i)
    if newlist:
        div_pages=newlist[-2]
    else:
        div_pages='1'  
 
    return div_pages
 
def getmovielist(html):
    soup=BeautifulSoup(html)
         
    divs=soup.find_all('ul',{'class':'mod_list_pic_130'})
    for div_html in divs:
        div_html = str(div_html).replace('\n','')
        getmovie(div_html)
 
def getmovie(html):
    global NUM
    global m_type
    global m_site
    re_movie = r'<li><a _hot=\"(.+?)\" class=\"mod_poster_130\" href=\"(.+?)\" target=\"_blank\" title=\"(.+?)\"><img.+?</li>'
    p=re.compile(re_movie,re.DOTALL)
    movies = p.findall(html)
    if movies:
        for movie in movies:
            NUM+=1
            print "%s:%d" %("="*70,NUM)
            values = dict(
                movie_title =movie[2],
                movie_url = movie[1],
                movie_site = m_site,
                movie_type = m_type
                )
            print movie[2]
            NUM+=1
            #print "%s : %d"%("="*70,NUM)
    else:
        print "movies it null"
 
#这个链接是免费的电影，0_0之前的值可选：012，分别代表最新，最火，好评
url = 'http://v.qq.com/list/1_-1_-1_-1_2_0_0_20_0_-1_0.html'
#url = 'http://v.qq.com/list/1_-1_-1_-1_1_0_0_20_0_-1_0.html'
#这个是要包含收费的： url = 'http://v.qq.com/list/1_-1_-1_-1_1_0_0_20_-1_-1_-1.html'
gettags(gethtml(url))
