from selenium.webdriver.common.by import By

COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

ORDER_BUTTON_TOP = (
    By.XPATH,
    "//button[contains(@class,'Button_Button') and contains(@class,'Button_Middle') and text()='Заказать']",
)

ORDER_BUTTON_BOTTOM = (
    By.XPATH,
    "//button[contains(@class,'Button_Button') and not(contains(@class,'Button_Middle')) and text()='Заказать']",
)

SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

def question_by_index(index: int):
    return (By.ID, f"accordion__heading-{index}")

def answer_by_index(index: int):
    return (By.XPATH, f"//div[@id='accordion__panel-{index}']//p")
