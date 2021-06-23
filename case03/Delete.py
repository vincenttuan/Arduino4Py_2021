import sqlite3

sql = 'DELETE FROM Lotto WHERE id=%d' % 1
print(sql)

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
cursor.execute(sql)
print("Delete ok, rowcunt:", cursor.rowcount)
conn.commit()
conn.close()