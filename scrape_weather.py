import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/151.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=options)

driver.set_page_load_timeout(60)

try:
    driver.get("https://www.timeanddate.com/weather/")
except TimeoutException:
    print("Page took too long to fully load, continuing.")

results = []

weather_rows = driver.find_elements(
    By.CSS_SELECTOR,
    "table.zebra.tb-theme tbody tr"
)

print("Rows found:", len(weather_rows))

for row in weather_rows:

    cells = row.find_elements(
        By.TAG_NAME,
        "td"
    )

    for i in range(0, len(cells), 4):

        if i + 3 >= len(cells):
            continue

        try:
            
            city = cells[i].find_element(
                By.TAG_NAME,
                "a"
            ).text

            
            local_time = cells[i + 1].text

            weather_image = cells[i + 2].find_element(
                By.TAG_NAME,
                "img"
            )

            condition = weather_image.get_attribute(
                "alt"
            )

            temperature = cells[i + 3].text

            weather_data = {
                "City": city,
                "Local Time": local_time,
                "Condition": condition,
                "Temperature": temperature
            }

            results.append(weather_data)

        except Exception as e:
            print("Skipped one city:", e)

driver.quit()

df = pd.DataFrame(results)

print(df)
print(df.shape)

df.to_csv(
    "weather_raw.csv",
    index=False
)



