import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.common.exceptions import TimeoutException
import time

path = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

url = "https://www.aljazeera.com/tag/israel-palestine-conflict/"

driver.get(url)

data = []

while True:
    # Parse the page source with BeautifulSoup
    bf = BeautifulSoup(driver.page_source, "html.parser")

    # Find the section containing the articles
    article_section = bf.find("section", id="news-feed-container")

    # Find all articles in the section
    all_news = article_section.find_all("article")

    # Process each article
    for news in all_news:
        headlines = news.find("a", class_="u-clickable-card__link").span.text
        descriptions = news.find("p").text
        dates = (
            news.find("div", class_="date-simple css-1yjq2zp")
            .span.text.replace("Published On ", "")
            .strip()
        )
        dates_object = datetime.strptime(dates, "%d %b %Y")
        dates_format = dates_object.strftime("%d-%m-%Y")
        # Check if the data is already in the list
        if (headlines, descriptions, dates_format) not in data:
            # Append the extracted information to the data list
            data.append((headlines, descriptions, dates_format))
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="news-feed-container"]/button',
                )
            )
        )
        show_more_button = driver.find_element_by_xpath(
            '//*[@id="news-feed-container"]/button'
        )

        # Scroll the "Show more" button into view
        driver.execute_script("arguments[0].scrollIntoView();", show_more_button)

        # Click the "Show more" button
        show_more_button.click()

        time.sleep(5)

    except TimeoutException:
        # Break the loop if the "Show more" button is not found
        print("No more articles to load.")
        break


df = pd.DataFrame(data, columns=["headline", "description", "date"])
df.to_csv("news_data.csv", index=False)
