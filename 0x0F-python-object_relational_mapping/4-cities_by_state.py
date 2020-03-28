#!/usr/bin/python3
"""cities by state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    conectDB = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db, port=3306)
    cur = conectDB.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    states = cur.fetchall()
    for i in states:
        print(i)
    cur.close()
    conectDB.close()
