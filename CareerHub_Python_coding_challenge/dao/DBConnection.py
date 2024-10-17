
    
import pyodbc

class DBConnection:
    @staticmethod
    def get_connection():
        try:
            connection_string = (
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=LUFFY\\SQLEXPRESS;'
                'DATABASE=CareerHubDB;'
                'Trusted_Connection=yes;'   
            )
            conn = pyodbc.connect(connection_string)
            print("Connection successful!")
            return conn
        except Exception as e:
            print(f"Database connection error: {e}")
            raise
