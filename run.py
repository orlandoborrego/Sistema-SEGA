from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

print("=" * 50)
print("DB_SERVER :", os.getenv("DB_SERVER"))
print("DB_NAME   :", os.getenv("DB_NAME"))
print("DB_USER   :", os.getenv("DB_USER"))
print("DB_PASS   :", "********" if os.getenv("DB_PASS") else "NO DEFINIDO")
print("HOST      :", os.getenv("HOST"))
print("=" * 50)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)