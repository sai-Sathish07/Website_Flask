import mysql.connector

def insertstudent(a,b,c,d,e,f):
    config = {
        'user': 'root',
        'password': 'sai1313',
        'host': 'localhost',
        'database': 'website'
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    sql=f"insert into studentweb values({a},'{b}',{c},'{d}','{e}','{f}')"
    print(sql)
    cursor.execute(sql)
    cnx.commit()
    cursor.close()
"""insertstudent(2,'sathish',1234568,'chennai','2024-10-05','2040-05-30')"""


def readingstudent(a):
    config = {
        'user': 'root',
        'password': 'sai1313',
        'host': 'localhost',
        'database': 'website'
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    sql=f"select *from studentweb where id={a}"
    cursor.execute(sql)
    for a in cursor.fetchall():
        print(a)
"""readingstudent(2)"""

def deletestudent(a):
    config = {
        'user': 'root',
        'password': 'sai1313',
        'host': 'localhost',
        'database': 'website'
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    sql=f"delete from studentweb where id={a}"
    cursor.execute(sql)
    cnx.commit()
"""deletestudent(2)"""