# pages/home_page.py
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    def click_order_button_top(self):
        self.click(HomePageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click(HomePageLocators.ORDER_BUTTON_BOTTOM)

    def click_faq_question(self, index):
        question_locator = HomePageLocators.faq_question(index)
        faq_section = self.driver.find_element(*HomePageLocators.FAQ_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_section)
        self.click(question_locator)

    def get_faq_answer_text(self, index):
        answer_locator = HomePageLocators.faq_answer(index)
        answer_element = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer_element.text