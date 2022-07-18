#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#import time, math
#
#try:
#    browser = webdriver.Chrome()
#    link = "https://SunInJuly.github.io/execute_script.html"
#    browser.get(link)
#    button = browser.find_element(By.TAG_NAME, "button")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#    button.click()
#    time.sleep(2)
#
#finally:
#    browser.quit()
#
#

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    url = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.ID, 'input_value').text
    answer = str(math.log(abs(12*math.sin(int(x)))))

    answer_form = browser.find_element(By.ID, 'answer')
    answer_form.send_keys(answer)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true)", robot_checkbox)
    robot_checkbox.click()

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    btn = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    btn.click()

    time.sleep(10)

finally:
    browser.quit()
