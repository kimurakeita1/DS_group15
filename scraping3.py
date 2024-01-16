import sqlite3
d = []
d_list =[]
# SQLiteデータベースに接続
conn = sqlite3.connect('scrap_data.db')
cursor = conn.cursor()
#17から31までのDateに対して、Date, Precipitations, Temperatures, Wind_speeds列の数値を取得するSQLクエリ
for date_value in range(17,32):
    query = f"SELECT Date, Precipitations, Temperatures, Wind_speeds FROM sql_DS WHERE Date = {date_value}"

    # SQLクエリを実行し、結果を取得
    cursor.execute(query)
    rows = cursor.fetchall()

    # 結果を変数に格納
    sum_a = 0
    sum_b = 0
    sum_c = 0
    sum_d = 0

    for row in rows:
        a, b, c, d = row
        sum_a += a
        sum_b += b
        sum_c += c
        sum_d += d

    # 平均値を計算
    count = len(rows)
    average_a = sum_a / count if count > 0 else 0
    average_b = sum_b / count if count > 0 else 0
    average_c = sum_c / count if count > 0 else 0
    average_d = sum_d / count if count > 0 else 0
    d = {
        'Date':average_a,
        'Precipitations': average_b,
        'Temperatures': average_c,
        'Wind_speeds':average_d
    }
    d_list.append(d)
# 1から13までのDateに対して、Date, Precipitations, Temperatures, Wind_speeds列の数値を取得するSQLクエリ
for date_value in range(1, 14):
    query = f"SELECT Date, Precipitations, Temperatures, Wind_speeds FROM sql_DS WHERE Date = {date_value}"

    # SQLクエリを実行し、結果を取得
    cursor.execute(query)
    rows = cursor.fetchall()

    # 結果を変数に格納
    sum_a = 0
    sum_b = 0
    sum_c = 0
    sum_d = 0

    for row in rows:
        a, b, c, d = row
        sum_a += a
        sum_b += b
        sum_c += c
        sum_d += d

    # 平均値を計算
    count = len(rows)
    average_a = sum_a / count if count > 0 else 0
    average_b = sum_b / count if count > 0 else 0
    average_c = sum_c / count if count > 0 else 0
    average_d = sum_d / count if count > 0 else 0
    d = {
        'Date':average_a,
        'Precipitations': average_b,
        'Temperatures': average_c,
        'Wind_speeds':average_d
    }
    d_list.append(d)

    # 結果を表示
    print(f"Average for Date {date_value}: {average_a}, Precipitations: {average_b}, Temperatures: {average_c}, Wind Speeds: {average_d}")

# 接続を閉じる
conn.close()

con = sqlite3.connect('scrap2_data.db')
cur = con.cursor()

sql_create_table_DS = 'CREATE TABLE IF NOT EXISTS sql_DS2 (Precipitations FLOAT, Temperatures FLOAT, Wind_speeds FLOAT);'
cur.execute(sql_create_table_DS)

for item in d_list:
    cur.execute('''
    INSERT INTO sql_DS2 (Precipitations, Temperatures, Wind_speeds) VALUES (?, ?, ?)''', (item['Precipitations'], item['Temperatures'], item['Wind_speeds']))

con.commit()



con = sqlite3.connect('scrap2_data.db')
cur = con.cursor()


cur.execute('SELECT * FROM sql_DS2')
rows = cur.fetchall()

for row in rows:
    Precipitations, Temperatures, Wind_speeds = row
    print(f'Precipitations: {Precipitations}, Temperatures: {Temperatures} Wind_speeds: {Wind_speeds}')

con.close()