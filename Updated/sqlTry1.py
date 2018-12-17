import sqlite3 as lite
import sys

con = lite.connect('paperstuff.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Paper(PaperName TEXT, Title TEXT, Summary TEXT)")
