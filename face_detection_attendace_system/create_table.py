'''
20-2-19
1.connecting to database creating needed tables


'''

import psycopg2
try:
    con = psycopg2.connect(user = "face_detection",
                                  password = "master@2510",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database="face_detection"
                                 )


    print("You are connected")
    create_table_query = '''CREATE TABLE student
             (ID serial PRIMARY KEY     NOT NULL,   
             name           TEXT    NOT NULL,
             roll_num    INT NOT NULL); '''
    cur = con.cursor()


    cur.execute(create_table_query)
    con.commit()


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)


