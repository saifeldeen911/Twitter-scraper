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
   
2. **Install required Python packages:**

You can use pip to install the necessary packages. It's recommended to use a virtual environment.

   ```bash
      git clone https://github.com/saifeldeen911/Twitter-scraper.git
      cd Twitter-scraper
   ```
3. **Download and set up ChromeDriver:**

Download ChromeDriver from ChromeDriver Downloads and ensure it's available in your system's PATH.

## Usage
1. **Run the script:**
   
   ```bash
      python twitter_scraper.py
   ```
2. **Input the required information:**

- Stock Symbol: Enter the stock symbol without the $ sign (e.g., AAPL).
- Time Interval: Enter the time interval in minutes for how often you want the script to scrape the accounts.

The script will continuously scrape the specified Twitter accounts at the given time interval and display the number of mentions of the stock symbol.

## How It Works

1. **Initialization:**

- The script initializes a headless Chrome WebDriver using Selenium.

2. **Scraping:**

- For each Twitter account URL, the script loads the page and scrolls down to load more tweets.
- It then searches for tweets mentioning the specified stock symbol using regular expressions.
  
3. **Reporting:**

- The script counts and reports the number of mentions of the stock symbol found in the tweets.
- It repeats the scraping process based on the user-defined time interval.

## Notes

- The script runs indefinitely until manually stopped. Ensure that you have the appropriate permissions and resources to run it.
- Modify the twitter_accounts list in the script to include the Twitter accounts you want to scrape.
- Adjust the time_interval to control how frequently the script performs scraping.
