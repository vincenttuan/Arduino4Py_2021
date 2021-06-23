import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../case03/demo.db')
df = pd.read_sql_query("SELECT NAME, SALARY FROM Employee", con=conn)
print(df)

# 繪圖
plt.plot(df.NAME.values, df.SALARY.values, 'r.')  # 點紅點
plt.plot(df['NAME'], df['SALARY'])  # 繪製折線圖
plt.show()

conn.close()