import sqlite3 as lite
import sys

con = lite.connect('paperstuff.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Paper")

    rows = cur.fetchall()
    counter = 0
    for row in rows:
        counter+=1
        if(counter>=5):
            break
        print(row)
        print('-----------------------------------------')
