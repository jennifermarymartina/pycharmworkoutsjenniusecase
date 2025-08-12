import mysql.connector
from dotenv import load_dotenv
import os
import csv
from datetime import datetime, date, time
import logging



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

def insertcustomerdata(con,custid,fullname,age,prof):
    if not conn:
        print("No database connection")
        return

    try:
        with conn.cursor() as cursor:
            createdby="jenni"
            custdata=[custid,fullname,age,prof,datetime.now(),createdby]
            insert_sql="""
            INSERT INTO tblcustomer_jenni(custid,fullname,age,profession,created_ts,created_by)
            VALUES(%s,%s,%s,%s,%s,%s)
            """
            print(insert_sql)
            print(custid)
            print(fullname)
            print(age)
            print(prof)
            cursor.execute(insert_sql, custdata)

            conn.commit()
            cursor.close()
            print("===Record Inserted===")
    except Exception as e:
        print(f"Error inserting customer data:{e}")

def execute_query(query, params=None):
    try:
        with conn.cursor() as cursor:

            cursor.execute(query, params or ())
            results = cursor.fetchall()

            return results
    except Error as e:
        logging.error(f"Error executing query: {e}")
        return None

if __name__=="__main__":
    conn=createconnection()
    custfile=open("C:\inceptez\pycharmworkouts\custs.txt","r")
    custfile.seek(0)
    custdata = custfile.readlines()
    print(custdata)
    if conn:

        for line in custdata:
            custinfo=line.split(",")
            custid=custinfo[0]
            custfname=custinfo[1]
            custlname=custinfo[2]
            age=custinfo[3]
            profession=custinfo[4]

            dbfullname = custfname.replace("'", "") + custlname.replace("'", "")

            dbcustid=custid.strip("'")
            dbfullname=custfname.replace("'","") + custlname.replace("'","")
            dbage=age

            dbprofession=profession.replace("\n", "")
            dbprofession=dbprofession.replace("'", "")

            print(str(dbprofession))
            #insertcustomerdata(conn, int(dbcustid),str(dbfullname), int(dbage), str(dbprofession))
        with open("C:\inceptez\pycharmworkouts\profcount.csv","w",encoding="utf-8",newline="") as csvfile:

            profcountquery="""
            select profession as Profession,count(*) as "Profession count" from tblcustomer_jenni group by profession
            """
            #profcountdata=execute_query(profcountquery)

            try:
                with conn.cursor() as cursor:

                    cursor.execute(profcountquery, None)
                    results = cursor.fetchall()



                    column_names = [col[0] for col in cursor.description]
                    print(column_names)
                    csvfile.write(",".join(column_names))
                    csvfile.write("\n")
                    for profrow in results:
                        row=str(profrow[0])+ "," +str(profrow[1])
                        print(row)

                        csvfile.write(row+"\n")

            except Exception as e:
                logging.error(f"Error executing query: {e}")





