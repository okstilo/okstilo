import time
from selenium import webdriver
from selenium.webdriver.common.by import By

articles = ["Python", "Ruby"]

driver = webdriver.Chrome()

for article in articles:
  driver.get("https://ja.wikipedia.org/wiki/" + article)
  driver.find_element(By.CSS_SELECTOR, ".infobox").screenshot("tmp/" + article + "_infobox.png")
  time.sleep(5.0)

driver.close()