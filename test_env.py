from dotenv import load_dotenv
import os

load_dotenv('.env')

print("DB_USER:", os.getenv('DB_USER'))
print("DB_PASS:", os.getenv('DB_PASS'))
print("DB_HOST:", os.getenv('DB_HOST'))
print("DB_NAME:", os.getenv('DB_NAME'))
