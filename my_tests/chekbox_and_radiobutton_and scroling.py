from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    driver.execute_script("window.scrollBy(0, 100);") #один вариант скролинга на 100

    value_x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(value_x)

    answer = driver.find_element(By.CSS_SELECTOR, ".form-control")
    answer.send_keys(y)

    checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    print("чек")

    radio_button = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    #driver.execute_script("return-arguments[0].scrollIntoView(true);", radio_button) #скрол до кнопки
    radio_button.click()
    print('радио')

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    # driver.execute_script("return-arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    print("Кнопка")


finally:
    time.sleep(10)

    driver.quit()