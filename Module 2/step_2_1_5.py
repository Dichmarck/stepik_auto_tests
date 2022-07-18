from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    url = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.ID, 'treasure').get_attribute("valuex")
    answer = str(math.log(abs(12*math.sin(int(x)))))

    answer_form = browser.find_element(By.ID, 'answer')
    answer_form.send_keys(answer)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    btn = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    btn.click()

    time.sleep(10)

finally:
    browser.quit()
