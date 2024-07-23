import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://orteil.dashnet.org/experiments/cookie/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get(URL)
cookie_found = driver.find_element(By.ID, value="cookie")


def browse_and_buy():
    best_price = 0
    current_index = 0
    # get money value
    money_found = driver.find_element(By.ID, value="money")
    try:
        current_money = int(money_found.text)
    except ValueError:
        current_money = int(money_found.text.replace(',', ''))

    # get hold of the store
    store_items = ["buyCursor", "buyGrandma", "buyFactory", "buyMine",
                   "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]

    for item in store_items:
        item_found = driver.find_element(By.ID, value=item)
        try:
            price = int(item_found.text.split('\n')[0].split(' ')[-1])
        except ValueError:
            price = int(item_found.text.split('\n')[0].split(' ')[-1].replace(',', ''))
        # print(price)

        # get hold of the best item to upgrade to
        if price > best_price:
            if current_money > price:
                best_price = price
                item_to_buy = store_items[current_index]
                current_index += 1

    click_to_buy = driver.find_element(By.ID, value=item_to_buy)
    click_to_buy.click()


if __name__ == "__main__":
    five_sec = time.time() + 5  # also starts the timer
    five_min = time.time() + 60*5  # 5 minutes
    while 1:
        cookie_found.click()
        if time.time() > five_sec:
            browse_and_buy()
            five_sec = time.time() + 5 
        if time.time() > five_min:  # approx 5 minutes
            cookies_per_second = driver.find_element(By.ID, value="cps")
            print(cookies_per_second.text)
            # driver.quit()
            break

# Angela Yu code - 60 cps
# mine - 76 cps
# TODO: make more efficient?
