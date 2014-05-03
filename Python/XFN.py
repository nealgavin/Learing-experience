
import sys
import urllib2
import HTMLParser
from BeautifulSoup import BeautifulSoup

URL = sys.argv[1]
XFN_TAGS = set([
'colleague',
'sweetheart',
'parent',
'co-worker',
'me',
'friend'
])
try:
	page = urllib2.urlopen(URL)
except urllib2.URLError:
	print 'fail to fetch' + item

try:
	soup = BeautifulSoup(page)
except HTMLParser.HTMLParseError:
	print 'fail to parse' + item
anchorTags = soup.findAll('a')
for a in anchorTags:
	if a.has_key('rel'):
		if len(set(a['rel'].split()) & XFN_TAGS) > 0:
			tags = a[ 'rel' ].split()
			print a.contents[0],a['href'],tags
