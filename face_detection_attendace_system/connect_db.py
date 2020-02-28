"""
21-2-19
connecting to databaseand creating cursor object to execute query

"""

import psycopg2 as pg

try:
    connection=pg.connect(user="face_detection",
                   password="master@2510",
                   host="127.0.0.1",
                   port="5432",
                   database="face_detection"
                   )

    cursor=connection.cursor()

except(Exception,pg.Error)as error:
    print("Error:",error)