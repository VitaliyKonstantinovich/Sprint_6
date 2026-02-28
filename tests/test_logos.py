# tests/test_logos.py
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urls
import locators.main_page_locators as L
from pages.main_page import MainPage

YANDEX_TARGET_URL = "https://yandex.ru/"

class TestLogos:
    @allure.title('Проверка клика по логотипу "Самокат"')
    def test_click_scooter_logo_opens_main_page(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.accept_cookies_if_present()
        page.click_order_button("top")
        page.click_scooter_logo()
        assert WebDriverWait(driver, 10).until(lambda d: d.current_url == urls.BASE_URL)

    @allure.title('Проверка факта открытия новой вкладки при клике по логотипу "Яндекс"')
    def test_yandex_logo_has_correct_link(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.accept_cookies_if_present()
        yandex_logo = page.wait_clickable(L.YANDEX_LOGO)
        actual_url = yandex_logo.get_attribute('href')
        assert actual_url == YANDEX_TARGET_URL

    @allure.title('Проверка редиректа на "Дзен" после перехода по ссылке из логотипа "Яндекс"')
    def test_click_yandex_logo_opens_dzen_in_new_tab(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.accept_cookies_if_present()
        original_window = driver.current_window_handle
        page.click_yandex_logo()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 30).until(
            EC.any_of(
                EC.title_contains("Дзен"),
                EC.title_contains("Яндекс")
            )
        )
        assert "dzen.ru" in driver.current_url

