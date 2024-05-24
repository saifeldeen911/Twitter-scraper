from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time


# Initialize the WebDriver with Chrome options
def init_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode for no GUI
    driver = webdriver.Chrome(options=options)

    return driver


# Scrape tweets for a specified stock symbol from a given Twitter URL
def twitter_scraper(driver, url, stock_symbol):
    try:
        driver.get(url)

        # Wait for the page to load completely
        time.sleep(5)

        # Scroll the page to load more tweets
        body = driver.find_element(By.TAG_NAME, "body")

        # Scroll the page 5 times
        for _ in range(5):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

        # Find tweets on the page
        tweets = driver.find_elements(By.XPATH, "//div[contains(@data-testid, 'tweetText')]")

        # Count the mentions of the stock symbol 
        mentions = 0
        for tweet in tweets:

            # using regular expression to find the stock symbol starting with Cashtag within the tweet text(case-insensitive)
            if re.search(r'\$\b' + re.escape(stock_symbol) + r'\b', tweet.text, re.IGNORECASE):
                # Increment the mention count if the stock symbol is found
                mentions += 1

        return mentions
    # Error handling when scraping url
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return 0


if __name__ == '__main__':

    driver = init_driver()

    try:

        # A list of twitter accounts to scrape
        twitter_accounts = [
            "https://twitter.com/Mr_Derivatives",
            "https://twitter.com/warrior_0719",
            "https://twitter.com/ChartingProdigy",
            "https://twitter.com/allstarcharts",
            "https://twitter.com/yuriymatso",
            "https://twitter.com/TriggerTrades",
            "https://twitter.com/AdamMancini4",
            "https://twitter.com/CordovaTrades",
            "https://twitter.com/Barchart",
            "https://twitter.com/RoyLMattox"
        ]

        # Prompt user to enter the stock symbol and scrape interval
        stock_symbol = input("Enter the stock symbol without $: ").upper()
        time_interval = int(input("Enter the time interval for scraping in minutes: ")) * 60

        # Repeatedly scrapes the accounts at the specified time interval
        while True:
            total_mentions = 0
            for account in twitter_accounts:
                # gets the mention count from all the accounts and prints the result
                total_mentions += twitter_scraper(driver, account, stock_symbol)

            print(f"'${stock_symbol}' was mentioned {total_mentions} times in the last {time_interval // 60} minutes.")

            time.sleep(time_interval)

    finally:
        driver.quit()
