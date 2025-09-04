# tests/test_order.py
import allure
import pytest
from datetime import datetime, timedelta
from pages.home_page import HomePage
from pages.order_page import OrderPage

@allure.feature("Order Process")
class TestOrder:
    @allure.title("Оформление заказа через {entry_point} кнопку")
    @pytest.mark.parametrize("entry_point", ["top", "bottom"])
    @pytest.mark.parametrize("test_data", [
        {
            "first_name": "Иван",
            "last_name": "Иванов",
            "address": "Москва, Тверская ул., 1",
            "metro": "Тверская",
            "phone": "+79991234567",
            "date": "10.09.2029",  # Фиксированная дата
            "period": "трое суток",
            "color": "black",
            "comment": "Позвонить за час"
        },
        {
            "first_name": "Мар",
            "last_name": "Петр",
            "address": "Санкт-Петербург, Невский пр., 100",
            "metro": "Невский проспект", 
            "phone": "+79997654321",
            "date": "11.09.2029",
            "period": "сутки",
            "color": "grey",
            "comment": "Оставить у двери"
        }
    ])
    def test_successful_order_creation(self, driver, base_url, entry_point, test_data):
        home_page = HomePage(driver, base_url)
        order_page = OrderPage(driver, base_url)
        
        with allure.step("Открыть главную страницу"):
            home_page.open()
            home_page.accept_cookies()
        
        with allure.step(f"Нажать кнопку 'Заказать' ({entry_point})"):
            if entry_point == "top":
                home_page.click_order_button_top()
            else:
                home_page.click_order_button_bottom()
        
        with allure.step("Заполнить информацию о пользователе"):
            order_page.fill_personal_info(
                test_data["first_name"],
                test_data["last_name"], 
                test_data["address"],
                test_data["metro"],
                test_data["phone"]
            )
        
        with allure.step("Заполнить информацию об аренде"):
            order_page.fill_rental_info(
                test_data["date"],
                test_data["period"],
                test_data["color"],
                test_data["comment"]
            )
        
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверить успешное оформление заказа"):
            assert order_page.is_order_successful(), "Не отображается окно успешного оформления заказа"