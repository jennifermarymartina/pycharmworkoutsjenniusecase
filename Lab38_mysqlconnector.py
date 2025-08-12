#pip install mysql-connector-python
#pip install python -dotenv
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


conn=None
try:

    conn = mysql.connector.connect(host=os.getenv('MYSQL_SERVERNAME'),
                                   user=os.getenv('MYSQL_USERNAME'),
                                   password=os.getenv('MYSQL_PASSWORD'),
                                   database=os.getenv('MYSQL_DBNAME'))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tblcustomer")
    results = cursor.fetchall()

    print("Total Rows:",cursor.rowcount)
    print("===========================")
    for row in results:

        print(row)
        print("CustID:",row[0])
        print("FirstName:",row[1])
        print("LastEmail:",row[2])
        print("Age:",row[3])
        print("Profession:",row[4])

    cursor.close()
    conn.close()

except Exception as e:
    print("Error",e)

finally:

    if conn !=None:
        conn.close()
        print("Connection closed")