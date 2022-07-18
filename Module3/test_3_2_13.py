import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test_1_6(unittest.TestCase):

    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name_form = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
        first_name_form.send_keys("Imya")
        last_name_form = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
        last_name_form.send_keys("familia")
        email = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
        email.send_keys("email@email.email")

        button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         f"Congratulation text not found. ")

        time.sleep(1)
        browser.quit()

    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name_form = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
        first_name_form.send_keys("Imya")
        last_name_form = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
        last_name_form.send_keys("familia")
        email = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
        email.send_keys("email@email.email")

        button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         f"Congratulation text not found. ")

        time.sleep(1)
        browser.quit()


