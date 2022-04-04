import allure

from pages.login_page import LoginPage

@allure.suite('Authorization testing')
@allure.description("Successful login by entering the correct data")
def test_successful_login(driver):
    link = "https://www.bodum.com/gb/en/"
    page = LoginPage(driver, link)
    page.open()
    page.open_personal_account()
    page.login_in("test@example.com", "123456")
    page.should_be_successful_login_message()

@allure.suite('Authorization testing')
@allure.description("Unsuccessful login by entering incorrect data")
def test_login_with_incorrect_data(driver):
    link = "https://www.bodum.com/gb/en/"
    page = LoginPage(driver, link)
    page.open()
    page.open_personal_account()
    page.login_in("incorrect@example.com", "no")
    page.should_be_unsuccessful_login_message()
