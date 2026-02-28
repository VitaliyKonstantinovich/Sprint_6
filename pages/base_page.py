# pages/base_page.py
import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Открываем URL: {url}')
    def open(self, url: str):
        self.driver.get(url)
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    @allure.step('Ожидаем видимости элемента')
    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидаем кликабельности элемента')
    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Скроллим к элементу')
    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Безопасный клик по элементу')
    def safe_click(self, locator):
        element = self.wait_clickable(locator)
        self.scroll_to(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод текста "{text}" в поле')
    def type_text(self, locator, text: str):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Отправляем клавиши в поле')
    def send_keys(self, locator, keys):
        element = self.wait_visible(locator)
        element.send_keys(keys)
