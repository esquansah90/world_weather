CTD Capstone Project Python Essentials

# World Weather Web Scraping Capstone

## Project Overview

This project collects current weather information from the
Weather Around the World website using Selenium.

The scraped dataset includes:

- City
- Local Time
- Weather Condition
- Temperature

The goal of the project is to scrape weather data, clean and transform
the data using Pandas, store the data in a SQLite database, and eventually
create an interactive Streamlit dashboard.

## Current Progress

For this stage of the project, I have:

- Used Selenium to scrape weather data from the website
- Collected weather information for approximately 140 cities
- Saved the raw data to `weather_raw.csv`
- Loaded the raw data using Pandas
- Checked for missing values and duplicate records
- Cleaned the Temperature column
- Converted temperature values from strings to numeric values
- Saved the cleaned data to `weather_clean.csv`

## Files

- `scrape_weather.py` - Scrapes weather data from the website
- `clean_weather.py` - Cleans and transforms the scraped data
- `weather_raw.csv` - Original scraped data
- `weather_clean.csv` - Cleaned weather data
