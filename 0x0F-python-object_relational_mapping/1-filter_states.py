#!/usr/bin/python3
"""
The script lists all states with name
starting with N
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
           ORDER BY states.id ASC ")

    rows_selected = cursor.fetchall()

    for row in rows_selected:
        print(row)
