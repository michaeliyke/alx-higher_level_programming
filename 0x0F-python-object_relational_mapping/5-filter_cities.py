#!/usr/bin/python3
"""State Selecting module"""
# ./5-filter_cities.py michael aka hbtn_0e_4_usa Texas
if __name__ == "__main__":
    import MySQLdb
    from sys import argv as args

    if len(args) < 5:
        exit(1)
    state = args[4]
    details = dict(
        host="localhost", port=3306, user=args[1],
        passwd=args[2], db=args[3], charset="utf8",
    )

    conn = MySQLdb.connect(**details)
    cur = conn.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC
        """
    cur.execute(query, (state,))
    query_rows = list(cur.fetchall())
    i = 0
    size = len(query_rows)
    for row in query_rows:
        if row and i < size - 1:
            print(row[0], end=", ")
        else:
            print(row[0])
        i += 1

    cur.close()
    conn.close()
