from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os

try:
    url = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(url)

    btn1 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    btn1.click()

    browser.switch_to.alert.accept()
    time.sleep(1)

    x = browser.find_element(By.ID, 'input_value').text
    answer = math.log(abs(12*math.sin(int(x))))
    answer_form = browser.find_element(By.ID, 'answer')
    answer_form.send_keys(answer)

    btn2 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    btn2.click()

    time.sleep(10)


finally:
    browser.quit()
