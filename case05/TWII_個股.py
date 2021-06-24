import requests
import pandas as pd
from io import StringIO

symbol = "2330"
date = "20210624"
path = "https://www.twse.com.tw/exchangeReport/BWIBBU?response=csv&date=%s&stockNo=%s" % (date, symbol)

csv = requests.get(path).text
# "日期","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
data = csv.split('\r\n')
data = list(filter(lambda l: len(l.split(',')) == 7, data ))
data = "\n".join(data)
#print(data)
df = pd.read_csv(StringIO(data))
print(data)