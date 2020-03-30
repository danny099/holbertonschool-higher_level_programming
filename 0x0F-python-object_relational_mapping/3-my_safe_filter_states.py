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
    query = """SELECT * FROM states
        WHERE BINARY states.name = %s ORDER BY states.id"""
    cur.execute(query, (state,))
    states = cur.fetchall()
    for i in states:
        print(i)
    cur.close()
    conectDB.close()
