# pages/order_page.py
import allure
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
import locators.order_page_locators as L


class OrderPage(BasePage):
    @allure.step('Заполняем шаг 1 формы заказа')
    def fill_step_one(self, name: str, surname: str, address: str, metro: str, phone: str) -> None:
        self.type_text(L.NAME_INPUT, name)
        self.type_text(L.SURNAME_INPUT, surname)
        self.type_text(L.ADDRESS_INPUT, address)

        self.type_text(L.METRO_INPUT, metro)
        self.safe_click(L.metro_option_by_text(metro))

        self.type_text(L.PHONE_INPUT, phone)
        self.safe_click(L.NEXT_BUTTON)

        self.wait_visible(L.DATE_INPUT)

    @allure.step('Заполняем шаг 2 формы заказа')
    def fill_step_two(self, rent_period: str, color: str, comment: str) -> None:
        tomorrow = datetime.now() + timedelta(days=1)
        date_str = tomorrow.strftime("%d.%m.%Y")

        self.type_text(L.DATE_INPUT, date_str)
        self.send_keys(L.DATE_INPUT, Keys.ENTER)

        self.safe_click(L.RENT_DROPDOWN)
        self.safe_click(L.rent_option_by_text(rent_period))

        if color == "black":
            self.safe_click(L.COLOR_BLACK)
        else:
            self.safe_click(L.COLOR_GREY)

        self.type_text(L.COMMENT_INPUT, comment)

    @allure.step('Подтверждаем заказ')
    def submit_order(self) -> None:
        self.safe_click(L.ORDER_BUTTON)
        self.safe_click(L.CONFIRM_YES_BUTTON)

    @allure.step('Проверяем успешное оформление заказа')
    def is_success_popup_shown(self) -> bool:
        self.wait_visible(L.SUCCESS_POPUP_HEADER)
        self.wait_visible(L.VIEW_STATUS_BUTTON)
        return True
