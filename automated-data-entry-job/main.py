import re
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://forms.gle/aKczNEZ8e1KKdcVw9"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

a_tags = soup.select(selector=".grid-search-results .StyledPropertyCardPhotoWrapper a")
apartment_listing = [tag.get("href") for tag in a_tags]

price_tags = soup.select(selector=".PropertyCardWrapper span")
price_listing = [price.getText() for price in price_tags]

price_listing_clean = [int(re.sub("[^0-9]", "", price_text))
                       for price_text in price_listing
                       if '/' in price_text or ',' in price_text
                       or '+' in price_text or '$' in price_text]

address_listing = soup.select(selector="a address")

address_listing_clean = [re.sub(" \|", ",", address.getText().strip())
                         for address in address_listing]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

for index in range(len(apartment_listing)):
    driver.get(FORM_URL)
    sleep(1)
    address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    submit_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    
    address_fill = driver.find_element(By.XPATH, value=address_xpath)
    address_fill.send_keys(f"{address_listing_clean[index]}")
    
    price_fill = driver.find_element(By.XPATH, value=price_xpath)
    price_fill.send_keys(f"${price_listing_clean[index]:,}")
    
    link_fill = driver.find_element(By.XPATH, value=link_xpath)
    link_fill.send_keys(f"{apartment_listing[index]}")
    
    submit_button = driver.find_element(By.XPATH, value=submit_xpath)
    submit_button.click()
    sleep(1)

driver.quit()
    
# TODO: Try and implement by sending in just key presses (tabs, type in entry, click enter)
