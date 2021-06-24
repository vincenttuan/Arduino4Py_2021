import requests
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

symbol = "2330"
date = "20210624"
path = "https://www.twse.com.tw/exchangeReport/BWIBBU?response=csv&date=%s&stockNo=%s" % (date, symbol)

csv = requests.get(path).text
# "日期","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
data = csv.split('\r\n')
data = list(filter(lambda l: len(l.split(',')) == 7, data )) # 過濾
data = "\n".join(data)  # 透過 \n 合併
#print(data)
df = pd.read_csv(StringIO(data))
df = df[df.columns[df.isnull().all() == False]] # 篩除不必要的欄位
print(df.dtypes)
#df = df.set_index('日期')
df = df.rename(columns={'殖利率(%)':'殖利率'})
df = df.rename(columns={'財報年/季':'財報年季'})
print(df)

plt.plot(df['日期'], df['殖利率(%)'])  # 繪製折線圖
plt.show()