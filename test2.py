__author__ = "Eggs"
 # _*_ coding: utf-8 _*_
import re
import urllib2
import time

t = time.localtime()
year = range(t[0],1989,-1)
season = range(4,0,-1)
url1 = "http://quotes.money.163.com/trade/lsjysj_zhishu_000001.html?year="
url2 = "&season="

urllist = []
for k in year:
	for v in season:
		urllist.append(url1 + str(k) + url2 + str(v))

def getData(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	content = response.read()
	pattern = re.compile('</thead[\s\S]*</td></tr></tr>')
	tab = re.findall(pattern, str(content))
	pattern = re.compile('>(.*?)<')
	data = re.findall(pattern, tab[0])

	return data

print(urllist[0])

print(getData(urllist[3]))

