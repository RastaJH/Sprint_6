import allure
import pytest
from data import BASE_URL
from pages.home_page import HomePage

@allure.feature("Navigation")
class TestNavigation:
    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirects_to_home(self, driver):
        home_page = HomePage(driver)
        
        home_page.open_main_page(BASE_URL)
        home_page.accept_cookies()
        home_page.click_order_button_top()
        home_page.click_scooter_logo()
        
        assert home_page.get_current_url() == BASE_URL

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        home_page = HomePage(driver)
        
        home_page.open_main_page(BASE_URL)
        home_page.accept_cookies()
        home_page.click_yandex_logo()
        home_page.switch_to_new_tab()
        
        current_url = home_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex.ru" in current_url