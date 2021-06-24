import requests

path = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20210623&selectType=ALL'
csv = requests.get(path).text
# "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
csv = csv.replace('"', '')
csv = csv.replace('-', '-1')
print(csv)
