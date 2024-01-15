import sqlite3

con = sqlite3.connect('local_data.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS sql_DS;')

sql_create_table_DS = 'CREATE TABLE IF NOT EXISTS sql_DS (Dates FLOAT, Times FLOAT);'
cur.execute(sql_create_table_DS)


Date = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
time_of_sleeping = [768, 515, 228, 201, 565, 0, 347, 723, 658, 434, 575, 493, 350, 616, 320, 399, 595, 490, 454, 530, 250,398,621,533,463,646,365,640]

d = list(zip(Date, time_of_sleeping))

for item in d:
    cur.execute('INSERT INTO sql_DS (Dates, Times) VALUES (?, ?)', (item[0], item[1]))
con.commit()

cur.execute('SELECT * FROM sql_DS')
rows = cur.fetchall()

for row in rows:
    Date, Times = row
    print(f'Date: {Date}, Times: {Times}')

con.close()
