from setup.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    ## class locators
    CART_ICON_LOCATOR = (By.CLASS_NAME, "shopping_cart_link")
    CART_PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, ".cart_item_label>a>.inventory_item_name")
    CART_PRODUCT_DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, ".cart_item_label>.inventory_item_desc")
    CART_PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, ".cart_item_label>div>.inventory_item_price")
    CONTINUE_SHOPPING_BUTTON_LOCATOR = (By.ID, "continue-shopping")

    ## class methods
    def get_cart_product_details(self):
        """The "get_cart_product_details" function returns a list with the name, description and price of the item that is present in the cart.
        Note: this function can be used if only one product is added to the cart.
        """

        cart_product_name = self.get_text(self.CART_PRODUCT_NAME_LOCATOR)
        cart_product_description = self.get_text(self.CART_PRODUCT_DESCRIPTION_LOCATOR)
        cart_product_price = self.get_text(self.CART_PRODUCT_PRICE_LOCATOR).strip('$')

        return cart_product_name, cart_product_description, cart_product_price
