#!/usr/bin/python3
"""State Selecting module"""
# ./2-my_filter_states.py michael aka hbtn_0e_0_usa 'Arizona'
if __name__ == "__main__":
    import MySQLdb
    from sys import argv as args

    user = args[1]
    password = args[2]
    db = args[3]
    name = args[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=db, charset="utf8")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(name))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row:
            print(row)
    cur.close()
    conn.close()
