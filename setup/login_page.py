from setup.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    ## class variables
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    INCORRECT_PASSWORD = "secret_labs"
    LOGIN_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
    HOME_PAGE_TITLE = "Swag Labs"

    ## class locators
    USERNAME_INPUT_LOCATOR = (By.ID, "user-name")
    PASSWORD_INPUT_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")
    LOGIN_ERROR_MESSAGE_LOCATOR = (By.XPATH, "//h3[@data-test='error']")
    HOME_PAGE_TITLE_LOCATOR = (By.CSS_SELECTOR, '.app_logo')

    ## class methods
    def set_username(self, username):
        self.type(self.USERNAME_INPUT_LOCATOR, username)

    def set_password(self, password):
        self.type(self.PASSWORD_INPUT_LOCATOR, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON_LOCATOR)

    def login_as_standard_user(self, username, password):
        self.wait_for_visibility(self.USERNAME_INPUT_LOCATOR)
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def get_home_page_title(self):
        self.wait_for_visibility(self.HOME_PAGE_TITLE_LOCATOR)
        return self.get_text(self.HOME_PAGE_TITLE_LOCATOR)