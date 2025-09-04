import allure
import pytest
from pages.home_page import HomePage
from locators.base_locators import BaseLocators

@allure.feature("Navigation")
class TestNavigation:
    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirects_to_home(self, driver, base_url):
        home_page = HomePage(driver, base_url)
        
        with allure.step("Открыть главную страницу и перейти к заказу"):
            home_page.open()
            home_page.accept_cookies()
            home_page.click_order_button_top()
        
        with allure.step("Нажать на логотип Самоката"):
            home_page.click(BaseLocators.SCOOTER_LOGO)
        
        with allure.step("Проверить возврат на главную страницу"):
            assert driver.current_url == base_url, "Не произошел переход на главную страницу по логотипу Самоката"

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_opens_dzen(self, driver, base_url):
        home_page = HomePage(driver, base_url)
        
        with allure.step("Открыть главную страницу"):
            home_page.open()
            home_page.accept_cookies()
        
        with allure.step("Нажать на логотип Яндекса"):
            home_page.click(BaseLocators.YANDEX_LOGO)
            home_page.switch_to_new_tab()
        
        with allure.step("Проверить открытие страницы Дзена"):
            current_url = driver.current_url
            assert "dzen.ru" in current_url or "yandex.ru" in current_url, f"Открыта неверная страница: {current_url}"
