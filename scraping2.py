import sqlite3

# データベースへの接続
con = sqlite3.connect('scrap_data.db')
cur = con.cursor()

#特定の文字を含む行を削除するSQL文
sql_delete_rows = "DELETE FROM sql_DS WHERE Times LIKE '%11.0%' OR Times LIKE '%12.0%' OR Times LIKE '%13.0%' OR Times LIKE '%14.0%' OR Times LIKE '%15.0%' OR Times LIKE '%16.0%' OR Times LIKE '%17.0%' OR Times LIKE '%18.0%' OR Times LIKE '%19.0%' OR Times LIKE '%20.0%' OR Times LIKE '%21.0%' OR Times LIKE '%22.0%';"

# SQL文を実行
cur.execute(sql_delete_rows)

# トランザクションのコミット
con.commit()

# データベースとの接続を閉じる
con.close()