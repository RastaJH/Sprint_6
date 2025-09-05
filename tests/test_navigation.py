# tests/test_navigation.py
import allure
import pytest
from pages.home_page import HomePage

@allure.feature("Navigation")
class TestNavigation:
    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirects_to_home(self, driver, base_url):
        home_page = HomePage(driver)
        
        with allure.step("Открыть главную страницу"):
            home_page.open_main_page(base_url)
            home_page.accept_cookies()
        
        with allure.step("Перейти к оформлению заказа"):
            home_page.click_order_button_top()
        
        with allure.step("Вернуться на главную по логотипу"):  # Используем метод страницы
            home_page.click_scooter_logo()  # ← ТЕПЕРЬ ПРАВИЛЬНО!
        
        with allure.step("Проверить URL главной страницы"):
            assert home_page.get_current_url() == base_url

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_opens_dzen(self, driver, base_url):
        home_page = HomePage(driver)
        
        with allure.step("Открыть главную страницу"):
            home_page.open_main_page(base_url)
            home_page.accept_cookies()
        
        with allure.step("Перейти на Дзен через логотип"):  # Используем метод страницы
            home_page.click_yandex_logo()  # ← ТЕПЕРЬ ПРАВИЛЬНО!
            home_page.switch_to_new_tab()
        
        with allure.step("Проверить открытие Дзен или Яндекса"):
            current_url = home_page.get_current_url()
            assert "dzen.ru" in current_url or "yandex.ru" in current_url