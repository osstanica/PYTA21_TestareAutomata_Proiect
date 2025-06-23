from selenium.webdriver.common.by import By
from setup.checkout_page import CheckoutPage
from setup.login_page import LoginPage
from setup.inventory_page import InventoryPage
from setup.product_page import ProductPage
from setup.cart_page import CartPage


class TestCheckoutPage(CheckoutPage, LoginPage, InventoryPage, ProductPage, CartPage):

    def test_checkout_process(self):

        ## login with the predefined user (the credentials are declared as constants in the LoginPage class) 
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)

        ## add a product to the shopping cart
        InventoryPage.add_product_to_cart(self)

        ## go to the shopping cart
        self.click_element(self.CART_ICON_LOCATOR)

        ## start the checkout process
        self.click_element(self.CHECKOUT_BUTTON_LOCATOR)

        ## insert the predefined shipping details (they are declared as constants in the CheckoutPage class) 
        self.insert_shipping_details()

        ## finalize the checkout process
        self.click_element(self.CONTINUE_BUTTON_LOCATOR)
        self.click_element(self.FINISH_BUTTON_LOCATOR)

        ## verify that the order was succesfully placed, based on the message displayed on the page
        fail_message_order_placed = "The message displayed after placing the order is not correct!"
        self.compare_test_with_reference(self.ORDER_PLACED_MESSAGE, self.get_text(self.ORDER_PLACED_MESSAGE_LOCATOR), fail_message_order_placed)

        ## verify that the user is correctly returned to the landing/inventory page
        self.click_element(self.BACK_HOME_BUTTON_LOCATOR)

        fail_message_back_home_button = "Inventory page was not successfully loaded after using the 'Back Home' button!"
        self.compare_test_with_reference(self.INVENTORY_PAGE_TITLE, LoginPage.get_landing_page_title(self), fail_message_back_home_button)


    def test_total_price_value(self):

        ## login with the predefined user (the credentials are declared as constants in the LoginPage class) 
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)

        ## add a product to the shopping cart and save the product's price
        inventory_item_position = InventoryPage.add_product_to_cart(self)
        product_price = self.driver.find_element(By.XPATH, f"{self.ITEM_PRICE_LOCATOR_BY_XPATH}[{inventory_item_position}]").text.strip('$')

        ## go to the shopping cart and then start the checkout process
        self.click_element(self.CART_ICON_LOCATOR)
        self.click_element(self.CHECKOUT_BUTTON_LOCATOR)

        self.insert_shipping_details()

        self.click_element(self.CONTINUE_BUTTON_LOCATOR)

        ## on the last page of the checkout process verify that the product's price is the same as the one from the inventory page and that the tax and the total cost are correctly computed
        item_total = self.get_text(self.PRICE_ITEM_TOTAL_LOCATOR).split('$')[1] # the total price value read from the application
        tax = self.get_text(self.PRICE_TAX_LOCATOR).split('$')[1] # the tax value read from the application
        tax_computed = round(float(product_price) * self.TAX_PERCENT, 2) # the tax value computed based on the item's price and the tax percent, defined as constants in the CheckoutPage class
        total = self.get_text(self.PRICE_TOTAL_LOCATOR).split('$')[1] # the total value read from the application

        fail_message_item_total = "The item price is not the same as in the inventory page!"
        self.compare_test_with_reference(product_price, item_total, fail_message_item_total)

        fail_message_tax = "The tax value displayed is not correctly calculated!"
        self.compare_test_with_reference(tax_computed, float(tax), fail_message_tax)

        fail_message_total = "The total value displayed is not correctly calculated!"
        self.compare_test_with_reference(round(float(product_price) + tax_computed, 2), float(total), fail_message_total)