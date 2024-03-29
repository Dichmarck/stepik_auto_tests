from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_form = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
    first_name_form.send_keys("Imya")
    last_name_form = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
    last_name_form.send_keys("familia")
    email = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
    email.send_keys("email@email.email")

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
