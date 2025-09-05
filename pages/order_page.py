# pages/order_page.py
import allure
import time
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Заполнить персональные данные")
    def fill_personal_info(self, first_name, last_name, address, metro_station, phone):
        self.send_keys(OrderPageLocators.FIRST_NAME, first_name)
        self.send_keys(OrderPageLocators.LAST_NAME, last_name)
        self.send_keys(OrderPageLocators.ADDRESS, address)

        # Исправленный выбор метро
        self.click(OrderPageLocators.METRO_INPUT)
        time.sleep(1)
        
        # Ищем станцию по названию
        metro_option = (By.XPATH, f"//div[contains(text(), '{metro_station}')]")
        self.click(metro_option)

        self.send_keys(OrderPageLocators.PHONE, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные аренды")
    def fill_rental_info(self, date, period, color, comment):
        date_field = self.driver.find_element(*OrderPageLocators.DATE_INPUT)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.RETURN)

        self.click(OrderPageLocators.RENTAL_PERIOD)
        time.sleep(1)
        
        period_option = (By.XPATH, f"//div[contains(text(), '{period}')]")
        self.click(period_option)

        color_locator = (By.ID, color)
        self.click(color_locator)

        self.send_keys(OrderPageLocators.COMMENT, comment)

        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить успешность заказа")
    def is_order_successful(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MODAL)