from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://amazon.com")

try:
    search_field = browser.find_element(
        by=By.CSS_SELECTOR, value="input#twotabsearchtextbox"
    )
    search_field.send_keys("Playstation")
    search_field.submit()

    time.sleep(2)  # let page load before scrolling
    page = browser.find_element(by=By.TAG_NAME, value="html")
    page.send_keys(Keys.END)  # scroll to the bottom

    time.sleep(3)
    page.send_keys(Keys.HOME)  # scroll back to the top
except Exception as e:
    print(f"error occured: {e}")

time.sleep(3)
browser.quit()
