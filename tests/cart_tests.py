
from selenium.webdriver.common.by import By
from setup.cart_page import CartPage
from setup.inventory_page import InventoryPage
from setup.login_page import LoginPage
from setup.product_page import ProductPage


class TestCartPage(CartPage, LoginPage, InventoryPage, ProductPage):

    def test_cart_value(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)

        inventory_item = InventoryPage.add_product_to_cart(self)
        inventory_item_name = self.driver.find_element(By.XPATH, f"{ProductPage.ITEM_NAME_LOCATOR_BY_XPATH}[{inventory_item}]").text
        inventory_item_description = self.driver.find_element(By.XPATH, f"{ProductPage.ITEM_DESCRIPTION_LOCATOR_BY_XPATH}[{inventory_item}]").text
        inventory_item_price = self.driver.find_element(By.XPATH, f"{ProductPage.ITEM_PRICE_LOCATOR_BY_XPATH}[{inventory_item}]").text.strip('$')

        product_info_from_inventory = [inventory_item_name, inventory_item_description, inventory_item_price]

        self.click_element(self.CART_ICON_LOCATOR)

        product_info_from_cart = self.get_cart_product_details()

        fail_message_product = "Product's info from the cart does not coincide with the info from the inventory page!"
        for i in range(len(product_info_from_inventory)):
            self.compare_test_with_reference(product_info_from_inventory[i], product_info_from_cart[i], fail_message_product)

        self.assert_errors()

    def test_continue_shopping_functionality(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)
        InventoryPage.add_product_to_cart(self)

        self.click_element(self.CART_ICON_LOCATOR)
        self.click_element(self.CONTINUE_SHOPPING_BUTTON_LOCATOR)

        fail_message_continue_shopping_button = "Inventory page was not successfully loaded after using the 'Continue shopping' button!"
        self.compare_test_with_reference(self.INVENTORY_PAGE_TITLE, LoginPage.get_home_page_title(self), fail_message_continue_shopping_button)

        self.assert_errors()
