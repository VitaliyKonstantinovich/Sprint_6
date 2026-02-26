import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

ORDER_CASES = [
    (
        "top",
        {
            "name": "Виталий",
            "surname": "Глебов",
            "address": "Москва, Тверская 1",
            "metro": "Черкизовская",
            "phone": "89990001122",
            "rent": "сутки",
            "color": "black",
            "comment": "Когорта 39. Позвоните заранее",
        },
    ),
    (
        "bottom",
        {
            "name": "Виталий",
            "surname": "Глебов",
            "address": "Москва, Арбат 10",
            "metro": "Черкизовская",
            "phone": "89990003344",
            "rent": "двое суток",
            "color": "grey",
            "comment": "Когорта 39. Оставьте у двери",
        },
    ),
]

class TestOrder:
    @pytest.mark.parametrize("entry, data", ORDER_CASES)
    def test_order_positive_flow(self, driver, entry, data):
        main = MainPage(driver)
        main.open_main()
        main.accept_cookies_if_present()
        main.click_order_button(entry)

        order = OrderPage(driver)
        order.fill_step_one(
            name=data["name"],
            surname=data["surname"],
            address=data["address"],
            metro=data["metro"],
            phone=data["phone"],
        )
        order.fill_step_two(
            rent_period=data["rent"],
            color=data["color"],
            comment=data["comment"],
        )
        order.submit_order()

        assert order.is_success_popup_shown()
