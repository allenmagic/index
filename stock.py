__author__ = "Eggs"
# coding: utf-8
import re,urllib2,time,csv,datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import matplotlib.dates as mpd

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

# get the number for date by date2num
def Date_no(strdate):
	t = time.strptime(strdate, "%Y-%m-%d")
	y,m,d = t[0:3]
	d = datetime.date(y, m, d)
	n = mpd.date2num(d)

	return n

# get the price data 
pr = []
for i in range(0,len(price),11):
	pr.extend([[
		Date_no(price[i])
		,float(price[i+1])
		,float(price[i+2])
		,float(price[i+3])
		,float(price[i+4])
		,float(price[i+8])]]
		)
		  
quotes = pr[0:80]

print(quotes)

fig,ax = plt.subplots(figsize=(30,6))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick_ohlc(ax,quotes,width=0.4,colorup='r',colordown='g')
plt.grid(False)
ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
plt.show()

