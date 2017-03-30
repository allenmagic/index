__author__ = "Eggs"
# _*_ coding: utf-8 _*_

import re
import urllib2

url = "http://quotes.money.163.com/trade/lsjysj_zhishu_000001.html"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read()

pattern = re.compile('</thead[\s\S]*</td></tr></tr>')
tab = re.findall(pattern,str(content))
pattern = re.compile('>(.*?)<')
price = re.findall(pattern, tab[0])

price_last = price[:]
for data in price:
	if data=='':
		price_last.remove('')

print("date","open","close")

for i in range(0,len(price_last),9):
	print(price_last[i],price_last[i+1],price_last[i+4])
