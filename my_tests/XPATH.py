from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/find_xpath_form")

    first_name = driver.find_element(By.XPATH, '//input[@name ="first_name"]')
    first_name.send_keys('Alex')
    last_name = driver.find_element(By.XPATH, '//input[@name="last_name"]')
    last_name.send_keys('Safra')
    city = driver.find_element(By.XPATH, '//input[@class="form-control city"]')
    city.send_keys('Yar')
    country = driver.find_element(By.XPATH, '//input[@id="country"]')
    country.send_keys('Bur')
    submit = driver.find_element(By.XPATH, '//div[6]/button[3]')
    submit.click()

finally:
    time.sleep(5)

    driver.quit()
