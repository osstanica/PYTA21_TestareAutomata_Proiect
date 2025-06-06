import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(unittest.TestCase):
    SAUCEDEMO_LOGIN_URL = "https://www.saucedemo.com/"

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get(self.SAUCEDEMO_LOGIN_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []

    def assert_errors(self):
        self.assertEqual([], self.verificationErrors)

    def tearDown(self):
        self.assert_errors()
        self.driver.quit()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def type(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))

    def compare_test_with_reference(self, reference_data, test_data, fail_message):
        try:
            self.assertEqual(reference_data, test_data)
        except AssertionError:
            self.verificationErrors.append(fail_message)
            print(f"Reference data: {reference_data}<p>")
            print(f"Test data: {test_data}<p>")
            print(f"FAIL message: {fail_message}\n")