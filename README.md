# Web Scraper for News Related to the Israel-Palestine Conflict

This Python web scraper collects news articles related to the Israel-Palestine conflict from the [Al Jazeera](https://www.aljazeera.com/tag/israel-palestine-conflict/) website. It utilizes Selenium for dynamic page loading and BeautifulSoup for HTML parsing.

## Dependencies

- [Pandas](https://pandas.pydata.org/): Data manipulation and analysis library
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): HTML parsing library
- [Selenium](https://www.selenium.dev/documentation/en/): Web testing library for browser automation

## Installation

1. Install the required Python libraries:

   ```bash
   pip install pandas beautifulsoup4 selenium
2. Download ChromeDriver from the official website: https://sites.google.com/chromium.org/driver/ and place it in the specified path.

## Usage

1. Run the `israel_palestine_news_scraper.py` script to collect news data.
2. The script will navigate to Al Jazeera's Israel-Palestine conflict page, scrape news articles, and save the data to a CSV file (`news_data.csv`).

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Dataset

[Kaggle](https://www.kaggle.com/datasets/emirslspr/israel-hamas-conflict-news-dataset/data)
