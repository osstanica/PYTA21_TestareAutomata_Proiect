import time

from setup.inventory_page import InventoryPage
from setup.login_page import LoginPage
from setup.product_page import ProductPage


class TestProductPage(ProductPage, LoginPage, InventoryPage):

    def test_product_details(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)
        product_info_from_inventory = self.get_details_and_open_product_page()
        product_info_from_product = [self.get_text(self.PRODUCT_NAME_LOCATOR), self.get_text(self.PRODUCT_DESCRIPTION_LOCATOR), self.get_text(self.PRODUCT_PRICE_LOCATOR).strip('$')]

        fail_message_product = "Product's info from the product's page does not coincide with the info from the inventory page!"
        for i in range(len(product_info_from_inventory)):
            self.compare_test_with_reference(product_info_from_inventory[i], product_info_from_product[i], fail_message_product)

        self.assert_errors()


    def test_return_to_inventory_page(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)
        self.get_details_and_open_product_page()

        self.click_element(self.BACK_TO_PRODUCTS_BUTTON_LOCATOR)

        fail_message_return_button = "Inventory page was not successfully loaded after using the 'Back to products' button!"
        self.compare_test_with_reference(self.INVENTORY_PAGE_TITLE, LoginPage.get_home_page_title(self), fail_message_return_button)

        self.assert_errors()