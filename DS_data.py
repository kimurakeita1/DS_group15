import sqlite3

# scrap2_dataからの接続
conn_source1 = sqlite3.connect('scrap2_data.db')
cursor_source1 = conn_source1.cursor()

# local_dataからの接続
conn_source2 = sqlite3.connect('local_data.db')
cursor_source2 = conn_source2.cursor()

# 新しいデータベースへの接続
conn_destination = sqlite3.connect('DS_data.db')
cursor_destination = conn_destination.cursor()

# 新しいデータベースにテーブルを作成
cursor_destination.execute('''
CREATE TABLE IF NOT EXISTS sql_DS3 (
    Precipitations INTEGER,
    Temperatures INTEGER,
    Wind_speeds INTEGER,
    Times INTEGER
)
''')

# scrap2_dataからPrecipitations, Temperatures, Wind_speedsのデータを抽出
cursor_source1.execute('SELECT Precipitations, Temperatures, Wind_speeds FROM sql_DS2')
data_to_insert_db1 = cursor_source1.fetchall()

# local_dataからtime_of_sleepingのデータを抽出
cursor_source2.execute('SELECT Times AS Times FROM sql_DS')
data_to_insert_db2 = cursor_source2.fetchall()

# 新しいデータベースにデータの挿入
for data_db1, data_db2 in zip(data_to_insert_db1, data_to_insert_db2):
    # バインディングの数が正しいことを確認してください
    cursor_destination.execute('INSERT INTO sql_DS3 (Precipitations, Temperatures, Wind_speeds, Times) VALUES (?, ?, ?, ?)',
                               (*data_db1, data_db2[0]))

# 変更を保存
conn_destination.commit()

# 接続を閉じる
conn_source1.close()
conn_source2.close()
conn_destination.close()