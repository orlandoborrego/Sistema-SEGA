import pyodbc
from dotenv import load_dotenv
import os

load_dotenv('.env')

server = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')

try:
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 18 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password};'
        f'TrustServerCertificate=yes;'
    )
    print("✅ Conexión exitosa a SQL Server")
    conn.close()
except Exception as e:
    print("❌ Error:", e)
