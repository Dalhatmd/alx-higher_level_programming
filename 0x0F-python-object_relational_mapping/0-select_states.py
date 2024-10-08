#!/usr/bin/python3
""" Script to list all states in a database """


import MySQLdb
import sys


def main():
    """Connects to a database and executes a command"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
