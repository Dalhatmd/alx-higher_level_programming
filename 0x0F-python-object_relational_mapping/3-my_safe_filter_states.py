#!/usr/bin/python3
""" a script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument. But this time,
    It is safe from MySQL injections!
    """
import MySQLdb
from sys import argv


def main():
    """ Main Function"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql_query = "SELECT * FROM states WHERE name=\
            BINARY %s ORDER BY states.id ASC"

    cur.execute(sql_query, (argv[4],))
    output = cur.fetchall()

    for row in output:
        print("{}".format(row))


if __name__ == "__main__":
    main()
