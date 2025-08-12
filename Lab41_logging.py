#pip install mysql-connector-python
#pip install python -dotenv
import mysql.connector
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(filename='mysql_query.log',level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
conn=None

try:

    conn = mysql.connector.connect(host=os.getenv("MYSQL_SERVERNAME"),
                               user=os.getenv("MYSQL_USERNAME"),
                               password=os.getenv("MYSQL_PASSWORD"),
                               database=os.getenv("MYSQL_DBNAME"))


    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tblcustomer")
    results = cursor.fetchall()
    print("Total rows:",cursor.rowcount)
    logging.info(f"Total rows: {cursor.rowcount}")
except Exception as e:
    print("Error",e)
    logging.error("Error connecting to MySQL database",e)
finally:
    if conn!=None:
        cursor.close()
        conn.close()
        print("Connection closed")
        logging.info("DB Connection closed")








conn.close()



#insertcustomerdata(conn,1003)


