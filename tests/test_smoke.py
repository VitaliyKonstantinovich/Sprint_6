# tests/test_smoke.py
import allure
from pages.main_page import MainPage

@allure.title('Проверка открытия главной страницы сервиса')
def test_open_main_page(driver):
    page = MainPage(driver)
    page.open_main()
    page.accept_cookies_if_present()
    assert True
