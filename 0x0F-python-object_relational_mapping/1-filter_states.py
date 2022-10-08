#!/usr/bin/python3
""" Python script that uses the module `MySQLdb`.

The script utilises the module to connect to a database and
return a list of the states starting with `N` from it.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=passwd, db=database)
    cur = db.cursor()
    query = """SELECT id, name FROM states
               WHERE name LIKE BINARY 'N%' ORDER BY id"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close
