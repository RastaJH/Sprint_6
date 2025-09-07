import allure
import pytest
from data import ORDER_DATA, BASE_URL
from pages.home_page import HomePage
from pages.order_page import OrderPage

@allure.feature("Order Process")
class TestOrder:
    @allure.title("Оформление заказа через верхнюю кнопку")
    @pytest.mark.parametrize("order", ORDER_DATA)
    def test_order_via_top_button(self, driver, order):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)

        home_page.open_main_page(BASE_URL)
        home_page.accept_cookies()
        home_page.click_order_button_top()

        order_page.fill_personal_info(
            order['first_name'], order['last_name'],
            order['address'], order['metro'], order['phone']
        )
        order_page.fill_rental_info(
            order['date'], order['period'],
            order['color'], order['comment']
        )
        order_page.confirm_order()

        assert order_page.is_order_successful()

    @allure.title("Оформление заказа через нижнюю кнопку")
    @pytest.mark.parametrize("order", ORDER_DATA)
    def test_order_via_bottom_button(self, driver, order):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)

        home_page.open_main_page(BASE_URL)
        home_page.accept_cookies()
        home_page.click_order_button_bottom()

        order_page.fill_personal_info(
            order['first_name'], order['last_name'],
            order['address'], order['metro'], order['phone']
        )
        order_page.fill_rental_info(
            order['date'], order['period'],
            order['color'], order['comment']
        )
        order_page.confirm_order()

        assert order_page.is_order_successful()