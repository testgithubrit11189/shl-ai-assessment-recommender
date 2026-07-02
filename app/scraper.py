from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.shl.com/solutions/products/product-catalog/")

time.sleep(5)

print(driver.title)

cards = driver.find_elements(By.TAG_NAME, "a")

print("Total links:", len(cards))

for i in cards[:20]:
    print(i.text, i.get_attribute("href"))

driver.quit()