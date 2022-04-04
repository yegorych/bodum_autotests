import allure

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("click on the button of your personal account")
    def open_personal_account(self):
        self.driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT).click()

    @allure.step("authorization")
    def login_in(self, email, password):
        self.driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOG_IN_BUTT).click()

    @allure.step("toast message about logging in")
    def should_be_successful_login_message(self):
        text_toast_message = self.driver.find_element(*LoginPageLocators.TOAST_MESSAGE).text
        assert "You have successfully logged in" in text_toast_message, "Successful login message did not appear"

    @allure.step("toast message about logging in")
    def should_be_unsuccessful_login_message(self):
        text_toast_message = self.driver.find_element(*LoginPageLocators.TOAST_MESSAGE).text
        assert "The account sign-in was incorrect or your account is disabled temporarily." in text_toast_message, "Unsuccessful login message did not appear"


