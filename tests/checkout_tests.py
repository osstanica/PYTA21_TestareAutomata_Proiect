from selenium.webdriver.common.by import By
from setup.checkout_page import CheckoutPage
from setup.login_page import LoginPage
from setup.inventory_page import InventoryPage
from setup.product_page import ProductPage
from setup.cart_page import CartPage


class TestCheckoutPage(CheckoutPage, LoginPage, InventoryPage, ProductPage, CartPage):

    def test_checkout_process(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)
        InventoryPage.add_product_to_cart(self)

        self.click_element(self.CART_ICON_LOCATOR)
        self.click_element(self.CHECKOUT_BUTTON_LOCATOR)

        self.insert_shipping_details()

        self.click_element(self.CONTINUE_BUTTON_LOCATOR)
        self.click_element(self.FINISH_BUTTON_LOCATOR)

        fail_message_order_placed = "The message displayed after placing the order is not correct!"
        self.compare_test_with_reference(self.ORDER_PLACED_MESSAGE, self.get_text(self.ORDER_PLACED_MESSAGE_LOCATOR), fail_message_order_placed)
        
        self.click_element(self.BACK_HOME_BUTTON_LOCATOR)

        fail_message_back_home_button = "Inventory page was not successfully loaded after using the 'Back Home' button!"
        self.compare_test_with_reference(self.INVENTORY_PAGE_TITLE, LoginPage.get_landing_page_title(self), fail_message_back_home_button)


    def test_total_price_value(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)
        inventory_item_position = InventoryPage.add_product_to_cart(self)
        product_price = self.driver.find_element(By.XPATH, f"{self.ITEM_PRICE_LOCATOR_BY_XPATH}[{inventory_item_position}]").text.strip('$')

        self.click_element(self.CART_ICON_LOCATOR)
        self.click_element(self.CHECKOUT_BUTTON_LOCATOR)

        self.insert_shipping_details()

        self.click_element(self.CONTINUE_BUTTON_LOCATOR)

        item_total = self.get_text(self.PRICE_ITEM_TOTAL_LOCATOR).split('$')[1]
        tax = self.get_text(self.PRICE_TAX_LOCATOR).split('$')[1]
        tax_computed = round(float(product_price) * self.TAX_PERCENT, 2)
        total = self.get_text(self.PRICE_TOTAL_LOCATOR).split('$')[1]

        fail_message_item_total = "The item price is not the same as in the inventory page!"
        self.compare_test_with_reference(product_price, item_total, fail_message_item_total)

        fail_message_tax = "The tax value displayed is not correctly calculated!"
        self.compare_test_with_reference(tax_computed, float(tax), fail_message_tax)

        fail_message_total = "The total value displayed is not correctly calculated!"
        self.compare_test_with_reference(round(float(product_price) + tax_computed, 2), float(total), fail_message_total)