__author__ = "Eggs"
# coding: utf-8
import re,urllib2,time,csv,datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import matplotlib.dates as mpd
import rpy2.robjects as rb


# get the data range include year & season
t = time.localtime()
year = range(t[0],1989,-1)
season = range(4,0,-1)


# get the get data function
def getData(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	content = response.read()

	pattern = re.compile('</thead[\s\S]*</tr>    </table>')
	ta = re.findall(pattern, str(content))
	pattern1 = re.compile("<td class='cGreen'>")
	pattern2 = re.compile("<td class='cRed'>")
	pattern3 = re.compile(",")
	tab1 = re.sub(pattern1,"<td>",str(ta))
	tab2 = re.sub(pattern2,"<td>",str(tab1))
	tab  = re.sub(pattern3, "", str(tab2))

	if len(tab) == 0:
		data = []
	else:
		pattern3 = re.compile('<td>(.*?)</td>')
		data = re.findall(pattern3, str(tab))

	for d in data:
		if d == '':
			data.remove('')

	return data

# get the data for code input
def get_stock_price(code):
	url1 = "http://quotes.money.163.com/trade/lsjysj_"
	url2 = ".html?year="
	url3 = "&season="
	urllist = []
	for k in year:
		for v in season:
			urllist.append(url1+str(code)+url2+str(k)+url3+str(v))
	
	price = []
	for url in urllist:
		price.extend(getData(url))
	return price

# get all histrocial data include all price and others
price = get_stock_price(600036)

		  
writer = csv.writer(file("stock.csv",'wb'))
writer.writerow(['Date','Open','High','Low','Close','Volume'])
pr = []
for i in range(0,len(price),11):
	pr.extend([[price[i],price[i+1],price[i+2],price[i+3],price[i+4],price[i+8]]])

for prl in pr:
	writer.writerow(prl)

rb.r.source('kgraph.R')



