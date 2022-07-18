import time, math, traceback
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    url_1 = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Chrome()
    browser.get(url_1)


    first_name_form = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    first_name_form.send_keys("Ivan")
    last_name_form = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    last_name_form.send_keys("Petrov")
    city_form = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    city_form.send_keys("Smolensk")
    country_form = browser.find_element(By.CSS_SELECTOR, '#country')
    country_form.send_keys("Russia")

    btn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    btn.click()

    time.sleep(10)

except Exception:
    traceback.print_exc()

finally:
    browser.quit()