#!/usr/bin/python3
""" Script that lists all cities in an input state """
import MySQLdb
from sys import argv


def main():
    """ Main func """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql_query = "SELECT cities.name FROM cities INNER JOIN states ON \
    cities.state_id = states.id WHERE states.name = %s"
    cur.execute(sql_query, (argv[4],))
    output = cur.fetchall()

    if output is not None:
        print(", ".join([row[0] for row in output]))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
