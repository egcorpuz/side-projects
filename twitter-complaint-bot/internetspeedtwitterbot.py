from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

# CHROME_DRIVER_PATH = "/Users/Gian/Development/chromedriver"
CONTRACT_DOWN_SPEED = 300
TWITTER_USER = os.environ["TWITTER_USER"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

SPEEDTEST_URL = "https://www.speedtest.net/"
X_URL = "https://x.com/i/flow/login"


class InterSpeedTwitterBot:
    
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get(SPEEDTEST_URL)
        go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[1]/a/span[4]')
        go_button.click()
        sleep(60)  # wait for the website to finish the speedtest
        new_url = self.driver.current_url
        # print(new_url)
        self.driver.get(new_url)
        download_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                  '2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div['
                                                                  '1]/div[1]/div/div[2]/span')
        upload_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                '2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div['
                                                                '1]/div[2]/div/div[2]/span')
        download_speed_flt = float(download_speed.text)
        upload_speed_flt = float(upload_speed.text)
        print("down:", download_speed_flt)
        print("up:", upload_speed_flt)
        self.down = download_speed_flt
        self.up = upload_speed_flt
    
    def tweet_at_provider(self):
        self.driver.maximize_window()
        self.driver.get(X_URL)
        sleep(5)
        email_fill = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                              '2]/div/div/div[2]/div[2]/div/div/div/div['
                                                              '4]/label/div/div[2]/div/input')
        email_fill.send_keys(TWITTER_USER, Keys.ENTER)
        sleep(3)
        pass_fill = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div['
                                                             '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                             '3]/div/label/div/div[2]/div[1]/input')
        pass_fill.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        sleep(5)
        post_fill = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                             '2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div['
                                                             '1]/div/div/div/div[2]/div['
                                                             '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                                             '1]/div/div/div/div/div/div[2]/div/div/div/div')
        message = (f"Hi @Converge_CSU,\n\nJust want to let you know that internet is relatively slow today: down speed "
                   f"of {self.down} MBps and up speed of {self.up}.\nMy net speed should be {CONTRACT_DOWN_SPEED} "
                   f"MBps.\n\n-Bot Test")
        post_fill.send_keys(message)
        sleep(3)
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                               '2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div['
                                                               '1]/div/div/div/div[2]/div[2]/div['
                                                               '2]/div/div/div/button/div/span/span')
        post_button.click()
    
    def quit_browser(self):
        self.driver.quit()
