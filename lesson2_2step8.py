from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_firstname = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    input_firstname.send_keys("Ivan")
    input_lastname = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    input_lastname.send_keys("Petrov")
    input_email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    input_email.send_keys("ipetrov@gmail.com")
    send_file = browser.find_element(By.CSS_SELECTOR, '#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    send_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

