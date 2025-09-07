from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")
    
    @staticmethod
    def faq_question(card):
        return (By.ID, f"accordion__heading-{card}")
    
    @staticmethod
    def faq_answer(card):
        return (By.ID, f"accordion__panel-{card}")