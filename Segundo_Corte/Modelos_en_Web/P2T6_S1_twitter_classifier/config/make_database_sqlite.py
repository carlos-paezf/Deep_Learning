import sqlite3
import os


if os.path.exists('tweets.sqlite'):
    os.remove('tweets.sqlite')

conn = sqlite3.connect('tweets.sqlite')
cursor = conn.cursor()
query = 'CREATE TABLE tweets_db (tweet TEXT, sentiment INTEGER, date TEXT)'
cursor.execute(query)

example1 = 'La cuarentena por el COVID es muy aburrida'
example2 = 'Estoy feliz de no sentir frio'

query = "INSERT INTO tweets_db (tweet, sentiment, date) VALUES (?,?,DATETIME('now'))"
cursor.execute(query, (example1, 2))
cursor.execute(query, (example2, 1))

conn.commit()


query_open = "SELECT * FROM tweets_db WHERE date BETWEEN '2021-01-01 11:11:11' AND DATETIME('now')"
cursor.execute(query_open)
results = cursor.fetchall()
print(results)


conn.close()