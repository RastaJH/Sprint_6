# locators/home_page_locators.py
from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")
    
    @staticmethod
    def faq_question(card):
        return (By.XPATH, f'//*[@id="accordion__heading-{card}"]')
    
    @staticmethod
    def faq_answer(card):
        return (By.XPATH, f'//*[@id="accordion__panel-{card}"]')