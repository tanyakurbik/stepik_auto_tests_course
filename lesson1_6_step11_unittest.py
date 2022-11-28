import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def registration(link):
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, ".first[required]")
    first_name.send_keys("Ivan")
    time.sleep(1)

    last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]")
    last_name.send_keys("Ivanov")
    time.sleep(1)

    email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
    email.send_keys("ivan@ivanov.ru")
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    return welcome_text


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        self.assertEqual(registration("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "Error text")

    def test_registration2(self):
        self.assertEqual(registration("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "Error text")


if __name__ == "__main__":
    unittest.main()


