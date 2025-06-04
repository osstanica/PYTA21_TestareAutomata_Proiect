from selenium.webdriver.common.by import By
from random import randint
from setup.inventory_page import InventoryPage
from setup.login_page import LoginPage
from setup.product_page import ProductPage


class TestProductPage(ProductPage, LoginPage, InventoryPage):

    def test_product_details(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)
        inventory_item_details = self.get_inventory_product_details()
        inventory_item_position = inventory_item_details[0]
        product_info_from_inventory = inventory_item_details[1:4]

        self.driver.find_element(By.XPATH, f"{self.ITEM_NAME_LOCATOR_BY_XPATH}[{inventory_item_position}]").click()
        product_info_from_product = [self.get_text(self.PRODUCT_NAME_LOCATOR), self.get_text(self.PRODUCT_DESCRIPTION_LOCATOR), self.get_text(self.PRODUCT_PRICE_LOCATOR).strip('$')]

        fail_message_product = "Product's info from the product's page does not coincide with the info from the inventory page!"
        for i in range(len(product_info_from_inventory)):
            self.compare_test_with_reference(product_info_from_inventory[i], product_info_from_product[i], fail_message_product)


    def test_return_to_inventory_page(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)

        list_all_item_names_elements = self.find_elements(InventoryPage.ITEMS_NAME_LOCATOR)
        max_number = len(list_all_item_names_elements)
        inventory_item_position = randint(1, max_number)

        self.driver.find_element(By.XPATH, f"{self.ITEM_NAME_LOCATOR_BY_XPATH}[{inventory_item_position}]").click()
        self.click_element(self.BACK_HOME_BUTTON_LOCATOR)

        fail_message_return_button = "Inventory page was not successfully loaded after using the 'Back to products' button!"
        self.compare_test_with_reference(self.INVENTORY_PAGE_TITLE, LoginPage.get_landing_page_title(self), fail_message_return_button)