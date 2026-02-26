import pytest
from pages.main_page import MainPage

FAQ_CASES = [
    (0, "Сутки — 400 рублей"),
    (1, "один заказ — один самокат"),
    (2, "Отсчёт времени аренды начинается"),
    (3, "Только начиная с завтрашнего дня"),
    (4, "Пока что нет"),
    (5, "Самокат приезжает к вам с полной зарядкой"),
    (6, "Да, пока самокат не привезли"),
    (7, "Да, обязательно"),
]

class TestFAQ:
    @pytest.mark.parametrize("index, expected_part", FAQ_CASES)
    def test_faq_answer_is_shown(self, driver, index, expected_part):
        page = MainPage(driver)
        page.open_main()
        page.accept_cookies_if_present()
        answer_text = page.open_faq_answer(index)
        assert expected_part in answer_text
