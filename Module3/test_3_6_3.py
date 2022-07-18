import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math


class Test_3_6_3:

    page_ids = ["236895", "236896", "236897", "236898", '236899', '236903', '236904', '236905']

    @pytest.mark.parametrize("page_id", page_ids)
    def test_enter_answer(self, browser, page_id):
        browser.implicitly_wait(5)
        browser.get(f"https://stepik.org/lesson/{page_id}/step/1")
        print(f"\nhttps://stepik.org/lesson/{page_id}/step/1")
        text_area = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
        answer = math.log(int(time.time()))
        text_area.send_keys(answer)
        btn = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        btn.click()
        result = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
        assert result == "Correct!", f"Неправильный ответ на странице с кодом {page_id}"


