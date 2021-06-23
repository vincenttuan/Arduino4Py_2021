# 請求出最高薪與最低薪的人名 ?
import sqlite3
sql = '''
        select 'MAX' AS TYPE, name, max(salary) as SALARY from Employee
        UNION ALL
        select 'MIN' AS TYPE, name, min(salary) as SALARY from Employee
    '''

conn = sqlite3.connect('../case03/demo.db')
cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)
