import math
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

STEPIK_LOGIN = os.getenv("STEPIK_LOGIN")
STEPIK_PASSWORD = os.getenv("STEPIK_PASSWORD")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number_lesson', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_guest_should_see_login_link(browser, number_lesson):
    link = f"https://stepik.org/lesson/{number_lesson}/step/1"
    browser.get(link)
    time.sleep(3)

    button_login = browser.find_element(By.ID, "ember32")
    button_login.click()
    time.sleep(2)

    input_email = browser.find_element(By.ID, "id_login_email")
    input_email.send_keys(STEPIK_LOGIN)
    input_password = browser.find_element(By.ID, "id_login_password")
    input_password.send_keys(STEPIK_PASSWORD)
    time.sleep(2)

    button_send = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    button_send.click()
    time.sleep(6)

    answer = math.log(int(time.time()))
    # breakpoint()
    input_answer = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
    input_answer.send_keys(answer)
    button_sendanswer = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button_sendanswer.click()
    time.sleep(3)
    correct_notation = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    assert correct_notation.text == "Correct!"
