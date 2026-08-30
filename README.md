# World Weather Web Scraping Capstone

## Project Overview

This project is a data pipeline that collects current weather information
from the Weather Around the World website.

The project uses Selenium to scrape weather data from the website, Pandas
to clean and transform the collected data, and SQLite to store the cleaned
data in a database.

The final goal of the project is to create an interactive Streamlit
dashboard that allows users to explore weather conditions and temperatures
for cities around the world.

## Data Collected

The scraped dataset contains weather information for approximately 140
cities around the world.

The dataset includes:

- City
- Local Time
- Weather Condition
- Temperature

## Project Workflow

The project follows this data pipeline:

1. Scrape current weather data from the website using Selenium.
2. Store the original scraped data in `weather_raw.csv`.
3. Load the raw CSV data into Pandas.
4. Inspect the data for missing values and duplicate records.
5. Clean and transform the weather data.
6. Save the cleaned data to `weather_clean.csv`.
7. Load the cleaned data into a SQLite database.
8. Query the SQLite database to verify that the data was stored correctly.
9. Use the cleaned weather data for analysis and visualization.
10. Create an interactive Streamlit dashboard.

## Data Cleaning

The raw weather data is cleaned using Pandas.

The cleaning process includes:

- Checking the structure and data types of the dataset
- Checking for missing values
- Checking for duplicate rows
- Removing duplicate records
- Removing the `°F` symbol and extra spaces from temperature values
- Converting temperature values from strings to numeric values
- Renaming the `Temperature` column to `Temperature_F`
- Rechecking the cleaned dataset for missing values

The cleaned dataset is saved as `weather_clean.csv`.

## SQLite Database

The cleaned weather data is stored in a SQLite database named
`weather.db`.

The `weather_database.py` script:

- Connects to the SQLite database
- Loads `weather_clean.csv` using Pandas
- Stores the cleaned data in a table named `weather`
- Checks that the `weather` table was created
- Queries the database to verify that weather records were stored correctly

The SQLite table contains:

- City
- Local Time
- Condition
- Temperature_F

## Files

- `scrape_weather.py` - Scrapes current weather data from the website using Selenium
- `clean_weather.py` - Cleans and transforms the raw weather data using Pandas
- `weather_database.py` - Loads the cleaned weather data into SQLite and verifies the stored records
- `weather_raw.csv` - Original data collected by the web scraper
- `weather_clean.csv` - Cleaned and transformed weather data
- `weather.db` - SQLite database containing the cleaned weather data
- `README.md` - Documentation for the project

## Technologies Used

- Python
- Selenium
- Pandas
- SQLite
- Git
- GitHub
- Streamlit (planned for the dashboard)

## Current Progress

Completed:

- Web scraping with Selenium
- Collection of weather data for approximately 140 cities
- Raw CSV creation
- Data inspection with Pandas
- Missing-value and duplicate checks
- Data cleaning and transformation
- Cleaned CSV creation
- SQLite database creation
- Loading cleaned data into SQLite
- Database verification using SQL queries

Next step:

- Continue analyzing the weather data
- Create visualizations
- Build the interactive Streamlit dashboard
