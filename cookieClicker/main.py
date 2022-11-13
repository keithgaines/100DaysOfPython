from selenium import webdriver



driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.amazon.com')



driver.quit()
