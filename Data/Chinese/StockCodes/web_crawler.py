import requests
from requests.exceptions import RequestException
import re
import json

# 深证 从深圳证券交易所官网下载的数据
f = open("sz.csv","r")
sz_codes = f.read().split("\n")
f.close()
sz_codes[0] = sz_codes[0][-6:]
sz_codes = ["1"+sz_codes[i] for i in range(len(sz_codes))]
# print(len(sz_codes))

# 上证 按照序号逐个尝试
def get_page_source(url):
    response = requests.get(url)
    if response.status_code == 200 and len(response.text) > len("_ntes_quote_callback({ });"):
        return response.text

sh_codes = []
for interval in range(600000,688982,100):
    print("Current Interval: "+ str(interval))
    for i in range(interval, interval+100):
        test_code = "0"+str(i)
        url = 'http://api.money.126.net/data/feed/'+test_code+',money.api'
        html = get_page_source(url)
        if html:
            sh_codes.append(test_code)

f = open("./codes.txt","w+")
f.write(",".join(sh_codes + sz_codes))
f.close()

        

