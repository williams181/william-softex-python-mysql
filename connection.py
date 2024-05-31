import mysql.connector
from config import config

class DBconnect:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor(buffered=True)
        
    def execute(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def fetch_all(self, query, values=None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    def disconnect(self):
        self.cursor.close()
        
    def service_status(self):
        return True
