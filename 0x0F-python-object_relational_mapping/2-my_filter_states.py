#!/usr/bin/python3
"""
    a script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    """
import MySQLdb
from sys import argv


def main():
    """ Main function """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name =\
            '{argv[4]}' ORDER BY states.id ASC")

    output = cur.fetchall()

    for row in output:
        print("{}".format(row))


if __name__ == "__main__":
    main()
