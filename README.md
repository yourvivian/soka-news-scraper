# soka-news-scraper

This project involves web scraping news articles from the Soka University website using the Python web scraping framework Scrapy. The goal is to extract information such as article titles, URLs, text content, categories, publication dates, and the date of scraping.

The project utilizes the scrapy library and extends the CrawlSpider class from Scrapy to define the web scraping behavior. The spider is named "soka-news" and is configured to crawl the "https://www.soka.edu/news-events/news" URL as the starting point.

## Usage

Navigate to the project directory: ```cd scraper```

Start the scraping process by running the following command: ```scrapy crawl soka-news -o articles.json```

The scraper will start fetching news articles from the Soka University website and store the extracted information in the output file articles.json.
