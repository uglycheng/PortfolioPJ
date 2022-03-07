import urllib
import urllib.request
import time
################################################################################################
# I Strongly suggest you to DELETE all the CSVs in this directory before downloading new CSVs  #
################################################################################################
codes = open("../StockCodes/codes.txt","r").read().split(",")
start_date = '20200101'
end_data = time.strftime('%Y%m%d',time.localtime())

for code in codes:
    try:
        print('正在获取股票%s数据'%code)
        url = 'http://quotes.money.163.com/service/chddata.html?code=%s&start=%s&end=%s'%(code,start_date,end_data)
        urllib.request.urlretrieve(url, "./"+code+'.csv')
    except:
        continue