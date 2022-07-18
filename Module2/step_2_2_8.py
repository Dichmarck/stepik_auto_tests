from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os

try:
    url = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(url)

    input_forms = browser.find_elements(By.TAG_NAME, 'input')
    for form in input_forms:
        if form.get_attribute('type') == 'file':
            form.send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__))), r'\bio.txt')
        else:
            form.send_keys('Abrakadabra')

    btn = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    btn.click()

    time.sleep(10)

finally:
    browser.quit()
