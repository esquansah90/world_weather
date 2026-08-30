import sqlite3
import pandas as pd

conn = sqlite3.connect("weather.db")

weather = pd.read_csv("weather_clean.csv")

print(weather.head())

weather.to_sql(
    "weather",
    conn,
    if_exists="replace",
    index=False
)

cursor = conn.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
""")

tables = cursor.fetchall()

print("\nTables in weather.db:")
for table in tables:
    print(table)

cursor.execute("""
    SELECT *
    FROM weather
    LIMIT 5
""")

rows = cursor.fetchall()

print("\nFirst 5 rows from the database:")
for row in rows:
    print(row)

conn.close()