# conftest.py
import os
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Чистим прокси
    for key in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
        os.environ.pop(key, None)

    options = webdriver.FirefoxOptions()

    # ВОЗВРАЩАЕМ СТРАТЕГИЮ 'EAGER' - "ЗОЛОТАЯ СЕРЕДИНА"
    # 'normal' - ждет всё, виснет на Дзене
    # 'none' (моя ошибка) - не ждет ничего, ломает все тесты на главной
    # 'eager' - ждет базовый HTML (кнопки/ссылки), но не картинки/скрипты. Идеально для нас.
    options.page_load_strategy = 'eager'
    
    # Настройки для стабильной работы Firefox
    options.set_preference("dom.popup_allowed_events", "click dblclick mousedown mouseup pointerdown pointerup")
    options.set_preference("privacy.trackingprotection.enabled", False)
    options.set_preference("privacy.trackingprotection.pbmode.enabled", False)
    options.set_preference("network.proxy.type", 0)

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
