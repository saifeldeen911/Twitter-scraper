# Twitter Scraper

A Python script for scraping tweets mentioning a specific stock symbol from multiple Twitter accounts using Selenium WebDriver. The script periodically checks the accounts and counts how many times the stock symbol is mentioned in tweets.

## Features

- Scrapes tweets from a list of Twitter accounts.
- Counts mentions of a specified stock symbol (cashtag) in the tweets.
- Runs in headless mode (no GUI) for efficient execution.
- Periodically scrapes at user-defined intervals.

## Prerequisites

- Python 3.x
- Selenium
- ChromeDriver (compatible with your version of Google Chrome)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/saifeldeen911/Twitter-scraper.git
   cd Twitter-scraper
