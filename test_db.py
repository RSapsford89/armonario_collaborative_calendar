import os
import psycopg2

# Load your env.py
if os.path.isfile('env.py'):
    import env

database_url = os.environ.get('DATABASE_URL')
print(f"Connecting to: {database_url[:50]}...")

try:
    conn = psycopg2.connect(database_url)
    print("✅ Database connection successful!")
    cursor = conn.cursor()
    cursor.execute('SELECT version();')
    db_version = cursor.fetchone()
    print(f"Database version: {db_version[0]}")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Database connection failed: {e}")