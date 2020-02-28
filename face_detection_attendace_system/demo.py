import psycopg2 as pg
import connect_db as con

def insert():
        insert = '''
            insert into dumy_student(name,roll_num,abc) values(%s,%s,%s) returning id

        '''
        rec = ["tas",123,890]
        con.cursor.execute(insert, rec)
        id = con.cursor.fetchone()

        con.connection.commit()
        return id



try:
    def print_data():
        con.cursor.execute("select * from dumy_student")
        rec = con.cursor.fetchall()
        for recc in rec:
            print(recc)

except(Exception, pg.Error)as error:
    print(error)
def take():
    name = input("name")
    id = input("id")
    col = input("college")
    rec = [name, id]
    rec.append(col)

    return rec
insert()

print_data()