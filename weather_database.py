import sqlite3
import pandas as pd

conn = sqlite3.connect("weather.db")

weather_raw = pd.read_csv("weather_raw.csv")
weather = pd.read_csv("weather_clean.csv")

print(weather.head())

weather_raw.to_sql(
    "weather_raw",
    conn,
    if_exists="replace",
    index=False
)

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
    FROM weather_raw
    LIMIT 5
""")

raw_rows = cursor.fetchall()

print("\nFirst 5 rows from weather_raw:")
for row in raw_rows:
    print(row)

cursor.execute("""
    SELECT *
    FROM weather
    LIMIT 5
""")

rows = cursor.fetchall()

print("\nFirst 5 rows from cleaned weather table:")
for row in rows:
    print(row)
    
print("\nDatabase verification complete.")

conn.close()