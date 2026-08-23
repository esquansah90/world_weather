import pandas as pd

# I loaded the raw data and checked the first 5 rows.
weather = pd.read_csv("weather_raw.csv")

print(weather.head())

# I checked the data types, the number of missing values, and duplicate rows.
weather.info()

print("\nMissing values:")
print(weather.isna().sum())

print("\nDuplicate rows:")
print(weather.duplicated().sum())

weather = weather.drop_duplicates()

# I removed the °F symbol and extra spaces. Then changed the Temperature column from string to numeric values.
weather["Temperature"] = (
    weather["Temperature"]
    .str.replace("°F", "", regex=False)
    .str.strip()
)

weather["Temperature"] = pd.to_numeric(
    weather["Temperature"],
    errors="coerce"
)

# I renamed the Temperature column to show that the temperature is in Fahrenheit
weather = weather.rename(
    columns={"Temperature": "Temperature_F"}
)

# I rechecked the first 5 rows, the data types, and the number of missing values after cleaning the data.
print("\nAFTER CLEANING")
print(weather.head())

weather.info()

print("\nMissing values after cleaning:")
print(weather.isna().sum())

# I saved the cleaned data into a CSV file
weather.to_csv(
    "weather_clean.csv",
    index=False
)