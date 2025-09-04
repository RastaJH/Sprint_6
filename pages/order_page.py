# pages/order_page.py
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    def fill_personal_info(self, first_name, last_name, address, metro_station, phone):
        self.send_keys(OrderPageLocators.FIRST_NAME, first_name)
        self.send_keys(OrderPageLocators.LAST_NAME, last_name)
        self.send_keys(OrderPageLocators.ADDRESS, address)
        
        self.click(OrderPageLocators.METRO_INPUT)
        metro_option = (By.XPATH, "(//li[@class='select-search__row'])[1]")
        self.wait.until(EC.element_to_be_clickable(metro_option))
        self.click(metro_option)
        
        self.send_keys(OrderPageLocators.PHONE, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_rental_info(self, date, rental_period, color, comment=None):
        self.click(OrderPageLocators.DATE_INPUT)
        date_field = self.driver.find_element(*OrderPageLocators.DATE_INPUT)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.click(OrderPageLocators.RENTAL_PERIOD)
        period_option = (By.XPATH, f"//div[text()='{rental_period}']")
        self.click(period_option)
        
        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)
        
        if comment:
            self.send_keys(OrderPageLocators.COMMENT, comment)
        
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    def is_order_successful(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MODAL)