#pip install mysql-connector-python
#pip install python -dotenv
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()



def createconnection():

    try:

        conn = mysql.connector.connect(host=os.getenv("MYSQL_SERVERNAME"),
                                   user=os.getenv("MYSQL_USERNAME"),
                                   password=os.getenv("MYSQL_PASSWORD"),
                                   database=os.getenv("MYSQL_DBNAME"))



    except Exception as e:
        print("Error",e)

    return conn



def getalldatabases(conn):
    print("==Database List==")
    cursor =conn.cursor()
    cursor.execute("SHOW DATABASES")
    dbs = cursor.fetchall()
    for db in dbs:
        print(db)
    cursor.close()

def getalltables(conn):
    cursor =conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("==Table List==")
    for table in tables:
        print(table)
    cursor.close()

def gettabledata(conn,tablename):
    cursor =conn.cursor()
    cursor.execute(f"select * from {tablename}")
    rows = cursor.fetchall()
    print(f"==Table Data : {tablename}==")
    for row in rows:
        print(row)
    cursor.close()

def insertcustomerdata(con,custid,fname,lname,age,prof):
    cursor = con.cursor()
    cursor.execute(f"insert into tblcustomer values({custid},'{fname}','{lname}',{age},'{prof}')")
    cursor._connection.commit()
    cursor.close()
    print("===Record Inserted===")

conn=createconnection()
getalldatabases(conn)
getalltables(conn)
gettabledata(conn,"tblcustomer")
#insertcustomerdata(conn,1005,"Bill","Gates",40,"Software")
#gettabledata(conn,"tblcustomer")
conn.close()



#insertcustomerdata(conn,1003)


