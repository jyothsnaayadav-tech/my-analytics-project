from sqlalchemy import create_engine, text

# Replace YOUR_PASSWORD with your PostgreSQL password
connection_string = "postgresql://jyothsnayadav:291204@localhost:5432/analytics_db"

try:
    engine = create_engine(connection_string)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ PostgreSQL connection successful!")
        print("🎉 DATABASE IS WORKING!")
except Exception as e:
    print(f"❌ Error: {e}")
    print("Check your password and database name!")