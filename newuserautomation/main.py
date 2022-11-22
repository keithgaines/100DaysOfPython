import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://admin.microsoft.com/#/homepage')

users = driver.find_element(By.NA, 'users')

users.click()

active_users = driver.find_element(By.NAME, 'Active users')
active_users.click()

add_user = driver.find_element(By.ID, 'UserListV2,addUserCommandBarButton')
add_user.click()

first_name = input("Please enter the user's first name")
last_name = input("Please enter the user's last name")



