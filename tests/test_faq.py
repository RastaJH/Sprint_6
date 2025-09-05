# tests/test_faq.py
import allure
import pytest
from data import FaqData
from pages.home_page import HomePage

@allure.feature("FAQ Section")
class TestFAQ:
    @allure.title("Тест вопросов и ответов в аккордеоне FAQ")
    @pytest.mark.parametrize('question_index, expected_text', FaqData.faq_questions)
    def test_faq_questions(self, driver, base_url, question_index, expected_text):
        home_page = HomePage(driver)
        
        home_page.open_main_page(base_url)
        home_page.accept_cookies()
        home_page.click_faq_question(question_index)
        actual_text = home_page.get_faq_answer_text(question_index)

        assert expected_text in actual_text