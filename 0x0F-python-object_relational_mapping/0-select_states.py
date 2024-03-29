#!/usr/bin/python3
"""State Selecting module"""
# ./0-select_states.py michael aka hbtn_0e_0_usa

if __name__ == '__main__':
    import MySQLdb
    from sys import argv as args

    user = args[1]
    password = args[2]
    db = args[3]

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
