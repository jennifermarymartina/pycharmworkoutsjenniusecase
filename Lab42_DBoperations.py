import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


#Load environment variables from .env file
load_dotenv()

#Configure logging
logging.basicConfig(
    filename='dboperations.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
class DBOperations:
    def __init__(self):
        try:
            host=os.getenv("MYSQL_SERVERNAME")
            user=os.getenv("MYSQL_USERNAME")
            password=os.getenv("MYSQL_PASSWORD")
            db=os.getenv("MYSQL_DBNAME")

            if not all([host,user,password,db]):
                raise ValueError("One or more required DB environment variables are missing")

            self.conn=mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=db,

            )
            self.cursor=self.conn.cursor()
            logging.info("Database connection established successfully ")

        except Error as e:
            logging.error(f"Error connecting to database: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

    def getalldatabases(self):
        try:
            logging.info("Fetching all databases")
            self.cursor.execute('SHOW DATABASES')
            databases=self.cursor.fetchall()


            for db in databases:
                print(db)
            logging.info("Databases fetched successfully")

        except Exception as e:
            logging.error(f"Error fetching databases: {e}")

    def getalltables(self):
        try:
            logging.info("Fetching all tables")
            self.cursor.execute('SHOW TABLES')
            tables=self.cursor.fetchall()
            for table in tables:
                print(table)
            logging.info("Tables fetched successfully")

        except Error as e:
            logging.error(f"Error fetching tables: {e}")

    def insert_customer(self,cust_data):
        try:
            insert_sql="""
            INSERT INTO tblcustomer(custid,fname,lname,age,profession)
            VALUES(%s,%s,%s,%s,%s)
            """
            self.cursor.executemany(insert_sql,cust_data)
            self.conn.commit()
            logging.info(f"Inserted {self.cursor.rowcount} customer records successfully")
        except Error as e:
            logging.error(f"Error inserting customer data: {e} ")

    def execute_query(self, query, params=None):
        try:
            logging.info(f"Executing query: {query}")
            self.cursor.execute(query, params or ())
            results = self.cursor.fetchall()
            logging.info("Query executed successfully.")
            return results
        except Error as e:
            logging.error(f"Error executing query: {e}")
            return None


    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
            logging.info("Database connection closed")
        except Error as e:
            logging.error(f"Error closing database: {e}")

class MySQLDatabase(DBOperations):

    def getdatabaseinfo(self):
            print("This is mysql server")



