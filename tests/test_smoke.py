from pages.main_page import MainPage

def test_open_main_page(driver):
    page = MainPage(driver)
    page.open_main()
    page.accept_cookies_if_present()
    assert True
