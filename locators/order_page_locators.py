from selenium.webdriver.common.by import By

NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
NEXT_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Далее']")

def metro_option_by_text(text: str):
    return (By.XPATH, f"//div[contains(@class,'select-search__select')]//div[text()='{text}']")

DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")

def rent_option_by_text(text: str):
    return (By.XPATH, f"//div[contains(@class,'Dropdown-option') and text()='{text}']")

COLOR_BLACK = (By.ID, "black")
COLOR_GREY = (By.ID, "grey")

COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[contains(@class,'Button_Middle') and text()='Заказать']")
CONFIRM_YES_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Да']")

SUCCESS_POPUP_HEADER = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")
VIEW_STATUS_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Посмотреть статус']")
