import finnhub
import json
import time
##################################################################################################
# I Strongly suggest you to DELETE all the JSONs in this directory before downloading new JSONs  #
##################################################################################################
with open('../../../apikey.txt') as f:
    api_key = f.read().strip('\n')
finnhub_client = finnhub.Client(api_key=api_key)
stock_symbol_info = finnhub_client.stock_symbols('US')
symbols = [i['symbol'] for i in stock_symbol_info]
start_struct_time = time.strptime("2020 01 01","%Y %m %d")
start_timestamp = int(time.mktime(start_struct_time))
end_timestamp = int(time.time())

for s in symbols:
    try:
        with open(s+'.json','w') as f:
            f.write((json.dumps(finnhub_client.stock_candles(s, 'D', start_timestamp, end_timestamp))))
    except:
        continue
