from setup.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):

    ## class variables
    FIRST_NAME = "Zoro"
    LAST_NAME = "Roronoa"
    ZIP_CODE = 1111
    ORDER_PLACED_MESSAGE = "Thank you for your order!"
    TAX_PERCENT = 0.08

    ## class locators
    CHECKOUT_BUTTON_LOCATOR = (By.ID, "checkout")
    FIRST_NAME_LOCATOR = (By.NAME, "firstName")
    LAST_NAME_LOCATOR = (By.ID, "last-name")
    ZIP_CODE_LOCATOR = (By.NAME, "postalCode")
    CONTINUE_BUTTON_LOCATOR = (By.ID, "continue")
    FINISH_BUTTON_LOCATOR = (By.ID, "finish")
    ORDER_PLACED_MESSAGE_LOCATOR = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON_LOCATOR = (By.ID, "back-to-products")
    PRICE_ITEM_TOTAL_LOCATOR = (By.CLASS_NAME, "summary_subtotal_label")
    PRICE_TAX_LOCATOR = (By.CLASS_NAME, "summary_tax_label")
    PRICE_TOTAL_LOCATOR = (By.CLASS_NAME, "summary_total_label")

    ## class methods
    def insert_shipping_details(self):
        self.wait_for_visibility(self.FIRST_NAME_LOCATOR)
        self.type(self.FIRST_NAME_LOCATOR, self.FIRST_NAME)
        self.type(self.LAST_NAME_LOCATOR, self.LAST_NAME)
        self.type(self.ZIP_CODE_LOCATOR, self.ZIP_CODE)