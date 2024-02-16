#!/usr/bin/env python3
import MySQLdb
import sys

arg = sys.argv
db = "hbtn_0e_0_usa"
password = "aka"
user = "michael"

if len(arg) > 1:
    user = arg[1]

if len(arg) > 2:
    password = arg[2]

if len(arg) > 3:
    db = arg[3]

conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                       passwd=password, db=db, charset="utf8")
cur = conn.cursor()
# HERE I have to know SQL to grab all states in my database
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
