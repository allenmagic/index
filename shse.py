__author__ = "Eggs"
 # _*_ coding: utf-8 _*_
import re
import urllib2
import time
import sys

# get date and make the season
t = time.localtime()
year = range(t[0],1989,-1)
season = range(4,0,-1)


# build the list of urls
url1 = "http://quotes.money.163.com/trade/lsjysj_zhishu_000001.html?year="
url2 = "&season="
urllist = []
for k in year:
	for v in season:
		urllist.append(url1 + str(k) + url2 + str(v))

# def the function to get data from page
def getData(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	content = response.read()

	pattern = re.compile('</thead[\s\S]*</tr>    </table>')
	tab = re.findall(pattern, str(content))
	if len(tab) == 0:
		data = []
	else:
		pattern1 = re.compile('<td>(.*?)</td>')
		data = re.findall(pattern1, tab[0])

	for d in data:
		if d == '':
			data.remove('')

	return data

# get the historical data
price = []
for url in urllist:
	price.extend(getData(url))

#print('Date','Open','Close')
for i in range(0,len(price),9):
	print(price[i],price[i+1],price[i+2],price[i+3],price[i+4])

