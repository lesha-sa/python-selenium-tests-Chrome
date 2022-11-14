from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Alex")

    last_name = driver.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Fry")

    email = driver.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("@ru")

    button = driver.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

    welcome_text = driver.find_element(By.TAG_NAME, "h1")
    welcome_text.eh = welcome_text.text
    assert "Congratulations! You have successfully registered!" == welcome_text.eh   # Проверка, что есть сообщение
    # об успешной регистрации

finally:
    time.sleep(5)

    driver.quit()