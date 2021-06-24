import sqlite3
'''
本益比(pe): 還本年限 <= 10
殖利率(r): >= 7%
股價淨值比(pb): 小於 1 適合買進, 大於等於 1 適合賣出
'''
bs = int(input('買進(1)賣出(2):'))
pe = float(input('請輸入本益比:'))
r  = float(input('請輸入殖利率:'))

# 殖利率(%)","本益比","股價淨值比
sql = '''
        select 證券代號, 證券名稱, 本益比, 殖利率, 股價淨值比 from Stock
        where (本益比 <= %.1f and 本益比 > 0) and 
              (殖利率 >= %.1f and 殖利率 > 0) and 
              (股價淨值比 %s 1 and 股價淨值比 > 0)
      ''' % (pe, r, '<' if bs == 1 else '>=')
print(sql)

conn = sqlite3.connect('twii.db')
cursor = conn.cursor()
cursor.execute(sql)
results = cursor.fetchall()

print('證券代號, 證券名稱, 本益比, 殖利率, 股價淨值比')
for result in results:
    print(result)

conn.close()
