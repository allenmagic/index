library(quantmod)

rm(list = ls())
setwd("~/GitHub/index/")
price <- as.xts(read.zoo("stock.csv",header=TRUE,sep=",",colClasses = c("Date", rep("numeric",5))))

n <- nrow(price)
m <- nrow(price)-100


#pdf(file = "k.pdf")
chartSeries(price[c(m:n)],theme = chartTheme("white"),up.col = "red",dn.col = "green",name = "600036",time.scale = 0.5,line.type = "l",bar.type = "ohlc",major.ticks='auto', minor.ticks=TRUE)

#dev.off()
