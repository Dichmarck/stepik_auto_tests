from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math, os

try:
    url = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(url)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    btn1 = browser.find_element(By.ID, 'book')
    btn1.click()

    time.sleep(1)

    x = browser.find_element(By.ID, 'input_value').text
    answer = math.log(abs(12*math.sin(int(x))))
    answer_form = browser.find_element(By.ID, 'answer')
    answer_form.send_keys(answer)

    btn2 = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn2)
    time.sleep(0.5)
    btn2.click()

    time.sleep(30)

finally:
    browser.quit()
