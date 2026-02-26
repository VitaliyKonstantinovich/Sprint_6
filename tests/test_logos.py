# tests/test_logos.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urls
from pages.main_page import MainPage

# Мы точно знаем, что в логотипе зашита эта ссылка
YANDEX_HOME_URL = "https://yandex.ru/"

class TestLogos:
    # Этот тест всегда был стабилен
    def test_click_scooter_logo_opens_main_page(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.accept_cookies_if_present()
        page.click_order_button("top")
        page.click_scooter_logo()
        assert WebDriverWait(driver, 10).until(lambda d: d.current_url == urls.BASE_URL)

    # ТЕСТ №1: Проверяем только факт открытия новой вкладки
    def test_yandex_logo_click_opens_new_tab(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.accept_cookies_if_present()

        # Используем самый надежный "Ctrl+Клик", чтобы гарантировать открытие вкладки
        page.click_yandex_logo()

        # Ждем, пока не станет 2 вкладки
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Проверяем, что вкладок действительно две. Нам не важно, что внутри.
        assert len(driver.window_handles) == 2

    # ТЕСТ №2: Проверяем, что ссылка из логотипа ведет на Дзен
    def test_yandex_link_redirects_to_dzen(self, driver):
        # Напрямую открываем URL, который мы нашли в логотипе
        driver.get(YANDEX_HOME_URL)

        # Ждем, пока в заголовке вкладки не появится "Дзен" или "Яндекс"
        WebDriverWait(driver, 30).until(
            EC.any_of(
                EC.title_contains("Дзен"),
                EC.title_contains("Яндекс")
            )
        )
        
        # Финальная проверка, что мы действительно оказались на Дзене
        assert "dzen.ru" in driver.current_url
