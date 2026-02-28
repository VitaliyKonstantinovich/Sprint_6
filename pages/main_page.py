# pages/main_page.py
import allure
import urls
import locators.main_page_locators as L
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открываем главную страницу')
    def open_main(self):
        self.open(urls.BASE_URL)
        self.wait_visible(L.ORDER_BUTTON_TOP)

    @allure.step('Принимаем куки, если плашка присутствует')
    def accept_cookies_if_present(self):
        try:
            self.safe_click(L.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass

    @allure.step('Кликаем по кнопке "Заказать": {entry}')
    def click_order_button(self, entry: str):
        if entry == "top":
            self.safe_click(L.ORDER_BUTTON_TOP)
        else:
            self.safe_click(L.ORDER_BUTTON_BOTTOM)

    @allure.step('Открываем ответ на вопрос: {index}')
    def open_faq_answer(self, index: int) -> str:
        self.safe_click(L.question_by_index(index))
        answer = self.wait_visible(L.answer_by_index(index))
        return answer.text

    @allure.step('Кликаем по логотипу Самоката')
    def click_scooter_logo(self):
        self.safe_click(L.SCOOTER_LOGO)

    @allure.step('Кликаем по логотипу Яндекса')
    def click_yandex_logo(self):
        self.safe_click(L.YANDEX_LOGO)
