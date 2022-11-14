from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/redirect_accept.html")

    submit_button = driver.find_element(By.CSS_SELECTOR, ".trollface.btn")
    submit_button.click()

    driver.switch_to.window(driver.window_handles[1])

    input_value = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    answer = calc(input_value)
    input_answer = driver.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(answer)

    submit_button_new_window = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit_button_new_window.click()

finally:
    time.sleep(15)

    driver.quit()