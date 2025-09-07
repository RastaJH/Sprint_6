import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_locators import BaseLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self, base_url):
        self.open(base_url)
    
    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.click(BaseLocators.COOKIE_ACCEPT)
    
    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click(HomePageLocators.ORDER_BUTTON_TOP)
    
    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.click(HomePageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Кликнуть на логотип Самоката") 
    def click_scooter_logo(self):
        self.click(BaseLocators.SCOOTER_LOGO)
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(BaseLocators.YANDEX_LOGO)
    
    @allure.step("Кликнуть на вопрос FAQ #{index}")
    def click_faq_question(self, index):
        locator = HomePageLocators.faq_question(index)
        self.click(locator)
    
    @allure.step("Получить текст ответа FAQ #{index}")
    def get_faq_answer_text(self, index):
        locator = HomePageLocators.faq_answer(index)
        return self.get_text(locator)