#!/usr/bin/python3
"""filter states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state = argv[4]
    conectDB = MySQLdb.connect(
        host='localhost', user=user, passwd=passwd, db=db, port=3306)
    cur = conectDB.cursor()
    query = """SELECT cities.name FROM cities, states
            WHERE BINARY states.name = %s
            AND cities.state_id = states.id
            ORDER BY cities.id"""
    cur.execute(query, (state,))
    states = cur.fetchall()
    print(", ".join([i[0] for i in cur]))
    cur.close()
    conectDB.close()
