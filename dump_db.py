import sqlite3
import csv

conn = sqlite3.connect('main.db')
c = conn.cursor()

query = "SELECT * FROM Users WHERE Users.phone IS NOT NULL"
c.execute(query)

with open('telegram_list.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in c.description])
    for row in c:
        writer.writerow(row)

conn.close()
