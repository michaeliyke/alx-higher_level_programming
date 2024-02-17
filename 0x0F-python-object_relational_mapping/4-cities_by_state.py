#!/usr/bin/python3
"""State Selecting module"""
# ./4-cities_by_state.py michael aka hbtn_0e_0_usa
if __name__ == "__main__":
    import MySQLdb
    from sys import argv as args

    user = args[1]
    password = args[2]
    db = args[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=db, charset="utf8")
    cur = conn.cursor()

    query = """
        SELECT cities.*, states.name AS state
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row:
            print(row)
    cur.close()
    conn.close()
