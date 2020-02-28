import psycopg2 as pg
import connect_db as con
import datetime as dt
import time
try:
    ts = time.time()
    date = dt.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    print(date)
    query="ALTER TABLE dumy_student add column "+date +" INT;"

    con.cursor.execute(query)
    con.connection.commit()
except (Exception,pg.Error) as error:
    print(error)