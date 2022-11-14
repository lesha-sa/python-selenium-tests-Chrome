from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time


link = "http://suninjuly.github.io/file_input.html"


try:
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Alex")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Safra")

    email = driver.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_2_2_step8 = os.path.join(current_dir, "download_file.py")
    select_file = driver.find_element(By.CSS_SELECTOR, "#file")
    select_file.send_keys(file_2_2_step8)

    #item = browser.find_element(By.XPATH, '//*[@type="file"]') еще вариант загрузки файла
    #item.send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt'))

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit_button.click()

finally:

    time.sleep(10)

    driver.quit()