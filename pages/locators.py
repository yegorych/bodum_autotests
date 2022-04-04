from selenium.webdriver.common.by import By


class LoginPageLocators():
  PERSONAL_ACCOUNT = (By.CLASS_NAME, "userPanel_customer")
  EMAIL = (By.NAME, "email")
  PASSWORD = (By.NAME, "password")
  NAME = (By.NAME, "name")
  LOG_IN_BUTT = (By.XPATH, "//*[@type='submit'][text()='Log In']")
  SIGN_UP_BUTT = (By.XPATH, "//*[@type='submit'][text()='Log In']")
  TOAST_MESSAGE = (By.CLASS_NAME, "Toastify__toast-body")
  SING_UP_LINK = (By.XPATH, "//*[text()='Sign Up']")
  CHECKBOX_PRIVACY_POLICY = (By.XPATH, "//*[@class='checkbox__display'][1]")
