import sqlite3
import requests
from bs4 import BeautifulSoup
import time
d=[]
d_list=[]
url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_a1.php?prec_no=45&block_no=1236&year=2023&month=12&day={}&view='
for t in range(17,32):
    urls = url.format(t)
    print(urls)
    r = requests.get(urls)
    time.sleep(1)
    soup = BeautifulSoup(r.text)
    contents = soup.find_all('tr',class_='mtx')[2:28]
    for i in range (24):
       content = contents[i]
       Date = t
       Time = content.find_all('td')[0].text
       Precipitation = content.find_all('td')[1].text
       Temperature = content.find_all('td')[2].text
       Wind_speed = content.find_all('td')[6].text
       d = {
            'Date':Date,
            'Times':Time,
            'Precipitations': Precipitation,
            'Temperatures': Temperature,
            'Wind_speeds':Wind_speed
        }
       d_list.append(d)
url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_a1.php?prec_no=45&block_no=1236&year=2024&month=1&day={}&view='
for t in range(1,14):
    urls = url.format(t)
    print(urls)
    r = requests.get(urls)
    time.sleep(1)
    soup = BeautifulSoup(r.text)
    contents = soup.find_all('tr',class_='mtx')[2:28]
    for i in range (24):
       content = contents[i]
       Date = t
       Time = content.find_all('td')[0].text
       Precipitation = content.find_all('td')[1].text
       Temperature = content.find_all('td')[2].text
       Wind_speed = content.find_all('td')[6].text
       d = {
            'Date':Date,
            'Times':Time,
            'Precipitations': Precipitation,
            'Temperatures': Temperature,
            'Wind_speeds':Wind_speed
        }
       d_list.append(d)
con = sqlite3.connect('scrap_data.db')
cur = con.cursor()

sql_create_table_DS = 'CREATE TABLE IF NOT EXISTS sql_DS (Date FLOAT, Times FLOAT, Precipitations FLOAT, Temperatures FLOAT, Wind_speeds FLOAT);'
cur.execute(sql_create_table_DS)

for item in d_list:
    cur.execute('''
    INSERT INTO sql_DS (Date, Times, Precipitations, Temperatures, Wind_speeds) VALUES (?, ?, ?, ?, ?)''', (item['Date'], item['Times'], item['Precipitations'], item['Temperatures'], item['Wind_speeds']))

con.commit()



con = sqlite3.connect('scrap_data.db')
cur = con.cursor()


cur.execute('SELECT * FROM sql_DS')
rows = cur.fetchall()

for row in rows:
    Date, Times, Precipitations, Temperatures, Wind_speeds = row
    print(f'Date: {Date},Times: {Times}, Precipitations: {Precipitations}, Temperatures: {Temperatures} Wind_speeds: {Wind_speeds}')

con.close()