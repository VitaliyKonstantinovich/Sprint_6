# pages/main_page.py
import urls
import locators.main_page_locators as L
from pages.base_page import BasePage

class MainPage(BasePage):
    def open_main(self):
        self.open(urls.BASE_URL)
        self.wait_visible(L.ORDER_BUTTON_TOP)

    def accept_cookies_if_present(self):
        try:
            self.safe_click(L.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass

    def click_order_button(self, entry: str):
        if entry == "top":
            self.safe_click(L.ORDER_BUTTON_TOP)
        else:
            self.safe_click(L.ORDER_BUTTON_BOTTOM)

    def open_faq_answer(self, index: int) -> str:
        question = self.wait_visible(L.question_by_index(index))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
        self.safe_click(L.question_by_index(index))
        answer = self.wait_visible(L.answer_by_index(index))
        return answer.text

    def click_scooter_logo(self):
        self.safe_click(L.SCOOTER_LOGO)

    def click_yandex_logo(self):
        # Обычный клик. Нам не важен переход, нам важно, что кнопка кликабельна.
        self.safe_click(L.YANDEX_LOGO)
