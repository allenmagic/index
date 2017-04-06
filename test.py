import time,datetime
#import matplotlib as mpl
#import matplotlib.dates as mpd

#p = ['2016-06-26','2016-06-27']
#def Date_no(strdate):
#	t = time.strptime(strdate, "%Y-%m-%d")
#	y,m,d = t[0:3]
#	d = datetime.date(y, m, d)
#	n = mpd.date2num(d)

#	return n

#print(Date_no(p[0]))

import rpy2.robjects as rb

rb.r("library('quantmod')")