from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollTo(0, 99)")

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)

    option_checkbox= browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option_checkbox.click()
    option_radio= browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option_radio.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")


    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

