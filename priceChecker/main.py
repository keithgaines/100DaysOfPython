from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.amazon.com/MAIORD-Wireless-Charger-Samsung-Charging/dp/B0B67HL68N/ref=sr_1_1_sspa?keywords=samsung+multi+charging+station&qid=1668094667&sprefix=samsung+multi%2Caps%2C151&sr=8-1-spons&psc=1')

price = driver.find_element(By.CLASS_NAME, "a-price")
print(price.text)

driver.quit()