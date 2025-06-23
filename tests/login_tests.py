from setup.login_page import LoginPage


class TestLoginPage(LoginPage):

    def test_login_incorrect_credentials(self):

        ## login with incorrect credentials
        self.login_as_standard_user(self.USERNAME, self.INCORRECT_PASSWORD)

        ## verify that the error message displayed is the expected one according to the business requirements
        in_app_login_error_message = self.get_text(self.LOGIN_ERROR_MESSAGE_LOCATOR)
        fail_message_login_incorrect_credentials = "Incorrect error message diaplayed after trying to login with incorrect credentials!"
        self.compare_test_with_reference(self.LOGIN_ERROR_MESSAGE, in_app_login_error_message, fail_message_login_incorrect_credentials)


    def test_login_correct_credentials(self):

        ## login with the predefined user (the credentials are declared as constants in the LoginPage class) 
        self.login_as_standard_user(self.USERNAME, self.PASSWORD)

        ## verify that the user is redirected to the landing/inventory page
        fail_message_login_correct_credentials = "Inventory page was not successfully loaded after the login action!"
        self.compare_test_with_reference(self.INVENTORY_PAGE_TITLE, self.get_landing_page_title(), fail_message_login_correct_credentials)
