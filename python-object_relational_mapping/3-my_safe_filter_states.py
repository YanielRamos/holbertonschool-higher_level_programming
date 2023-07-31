#!/usr/bin/python3
"""Lists all values in the states tables of a database where name
matches the argument in a safe way"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306,
    )
    state_name = sys.argv[4]

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", state_name)
    states = cur.fetchall()

    for state in states:
        print(state)
