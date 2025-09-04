import allure
import pytest
from data import FaqData
from pages.home_page import HomePage

@allure.feature("FAQ Section")
class TestFAQ:
    @allure.title("Тест вопросов и ответов в аккордеоне FAQ")
    @pytest.mark.parametrize('question_index, expected_text', FaqData.faq_questions)
    def test_faq_questions(self, driver, base_url, question_index, expected_text):
        home_page = HomePage(driver, base_url)
        
        with allure.step("Открыть главную страницу"):
            home_page.open()
            home_page.accept_cookies()
        
        with allure.step(f"Нажать на вопрос №{question_index + 1}"):
            home_page.click_faq_question(question_index)
        
        with allure.step("Проверить текст ответа"):
            actual_text = home_page.get_faq_answer_text(question_index)
            assert actual_text == expected_text, \
                f"Ожидался текст: '{expected_text}', но получен: '{actual_text}'"