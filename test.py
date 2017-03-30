__author__ = "Eggs"
 # _*_ coding: utf-8 _*_
import re
import urllib2
import time

t = time.localtime()
year = range(t[0],1989,-1)
months = range(12,0,-1)
url1 = "http://quotes.money.163.com/trade/lsjysj_zhishu_000001.html?year="
url2 = "&season="

urllist = []
for k in year:
	for v in months:
		urllist.append(url1 + str(k) + url2 + str(v))

def getData(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	content = response.read()

	pattern = re.compile('</thead[\s\S]*</td></tr></tr>')
	tab = re.findall(pattern,str(content))
	pattern = re.compile('>(.*?)<')
	raw_data = re.findall(pattern, tab[0])

	data = raw_data[:]
	for m in raw_data:
		if m == "":
			data.remove("")

	return data

price = []
for u in urllist:
	price.extend(getData(urllist[0]))

print("date","open","close")

for i in range(0,len(price),9):
	print(price[i])
