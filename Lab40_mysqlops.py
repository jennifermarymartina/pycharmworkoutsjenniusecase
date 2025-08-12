#pip install mysql-connector-python
#pip install python -dotenv
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()



def createconnection():
    conn =None
    try:

        conn = mysql.connector.connect(host=os.getenv("MYSQL_SERVERNAME"),
                                   user=os.getenv("MYSQL_USERNAME"),
                                   password=os.getenv("MYSQL_PASSWORD"),
                                   database=os.getenv("MYSQL_DBNAME"))

        return conn

    except Exception as e:
        print("Error",e)





def getalldatabases(conn):
    if not conn:
        print("No database connection")
        return
    print("==Database List==")
    cursor =conn.cursor()
    cursor.execute("SHOW DATABASES")
    dbs = cursor.fetchall()
    for db in dbs:
        print(db)
    cursor.close()

def getalltables(conn):
    if not conn:
        print("No database connection")
        return
    cursor =conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("==Table List==")
    for table in tables:
        print(table)
    cursor.close()

def gettabledata(conn,tablename):
    if not conn:
        print("No database connection")
        return
    try:

        cursor =conn.cursor()
        cursor.execute(f"select * from {tablename}")
        rows = cursor.fetchall()
        print(f"==Table Data : {tablename}==")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error fetching table data:{e}")

def insertcustomerdata(con,custid,fname,lname,age,prof):
    if not conn:
        print("No database connection")
        return

    try:
        with conn.cursor() as cursor:
            insert_sql="""
            INSERT INTO tblccustomer(custid,fname,lname,age,profession)
            VALUES(%s,%s,%s,%s,%s)
            """
            cursor.execute(insert_sql, custid,fname,lname,age,prof)
            cursor.commit()
            cursor.close()
            print("===Record Inserted===")
    except Exception as e:
        print("Error inserting customer data:{e}")

if __name__=="__main__":

    conn=createconnection()
    if conn:

        getalldatabases(conn)
        getalltables(conn)
        gettabledata(conn,"tblcustomer")
#insertcustomerdata(conn,1005,"Bill","Gates",40,"Software")
#gettabledata(conn,"tblcustomer")
conn.close()



#insertcustomerdata(conn,1003)


