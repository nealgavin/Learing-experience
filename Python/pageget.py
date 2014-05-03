import re
import urllib
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = r'src="(.*?\.gif)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	print imglist
	cnt = 1
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' %cnt)
		cnt += 1
if __name__ == '__main__':
	page = raw_input("get page")
	html = getHtml(page)
	getImg(html)

