'''
20-2-19
1.creating user
2.creating database with owner as current created user

'''

import psycopg2 as pg
try:
    conn=pg.connect(
        user="postgres",
        password="master@2510",
        host="127.0.0.1",
        port="5432"

    )
    if(conn):
        print("connect succes")
    cursor=conn.cursor()
    create_user='''
        create user face_detection with
        superuser
        createdb
        login
        password 'master@2510';
    '''
    create_db="create database face_detection owner face_detection"
    #cursor.execute(create_user)
    cursor.execute("END;") #to avoid blocking off error
    cursor.execute(create_db)
    conn.commit()
except(Exception,pg.Error)as error:
    print(error)
finally:
    if(conn):
        conn.close();
        print("connection close");