import requests

path = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20210623&selectType=ALL'
csv = requests.get(path).text
print(csv)

