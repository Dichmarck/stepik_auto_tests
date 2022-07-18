from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math

try:
    browser = webdriver.Chrome()
    url = "http://suninjuly.github.io/selects1.html"
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    answer = int(num1) + int(num2)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(str(answer))

    btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    btn.click()

    time.sleep(10)

finally:
    browser.quit()

