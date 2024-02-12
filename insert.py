import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Table created successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1, 'FAITH KARIMI',34, 340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2, 'LIAM MAINA', 69, 10000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3, 'TERRY WAIRIMU', 24, 240000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4, 'ALLAN NJERU',49, 250000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5, 'BERNICE NJERI', 25, 140000.00)")

conn.commit()
print("Employee inserted successfully")
conn.close()