from setup.login_page import LoginPage


class TestLoginPage(LoginPage):

    def test_login_incorrect_credentials(self):
        self.login_as_standard_user(self.USERNAME, self.INCORRECT_PASSWORD)

        in_app_login_error_message = self.get_text(self.LOGIN_ERROR_MESSAGE_LOCATOR)
        fail_message_login_incorrect_credentials = "Incorrect error message diaplayed after trying to login with incorrect credentials!"
        self.compare_test_with_reference(self.LOGIN_ERROR_MESSAGE, in_app_login_error_message, fail_message_login_incorrect_credentials)

        self.assert_errors()


    def test_login_correct_credentials(self):
        self.login_as_standard_user(self.USERNAME, self.PASSWORD)

        fail_message_login_correct_credentials = "Inventory page was not successfully loaded after the login action!"
        self.compare_test_with_reference(self.HOME_PAGE_TITLE, self.get_home_page_title(), fail_message_login_correct_credentials)

        self.assert_errors()
