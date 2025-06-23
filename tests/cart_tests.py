from selenium.webdriver.common.by import By
from setup.cart_page import CartPage
from setup.login_page import LoginPage
from setup.inventory_page import InventoryPage
from setup.product_page import ProductPage


class TestCartPage(CartPage, LoginPage, InventoryPage, ProductPage):

    def test_cart_details(self):

        ## login with the predefined user (the credentials are declared as constants in the LoginPage class)
        # print(self.login_as_standard_user.__doc__)
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)

        ## choose a product from the page, save its name, description and price into a list, and then add the product to the shopping cart
        # print(self.add_product_to_cart.__doc__)
        inventory_item_position = InventoryPage.add_product_to_cart(self)
        inventory_item_name = self.driver.find_element(By.XPATH, f"{ProductPage.ITEM_NAME_LOCATOR_BY_XPATH}[{inventory_item_position}]").text
        inventory_item_description = self.driver.find_element(By.XPATH, f"{ProductPage.ITEM_DESCRIPTION_LOCATOR_BY_XPATH}[{inventory_item_position}]").text
        inventory_item_price = self.driver.find_element(By.XPATH, f"{ProductPage.ITEM_PRICE_LOCATOR_BY_XPATH}[{inventory_item_position}]").text.strip('$')
        product_info_from_inventory = [inventory_item_name, inventory_item_description, inventory_item_price]

        ## go to the shopping cart
        self.click_element(self.CART_ICON_LOCATOR)
        # print(self.get_cart_product_details.__doc__)

        ## get the product's details from the shopping cart
        product_info_from_cart = self.get_cart_product_details()

        ## verify that the product's details saved from inventory page are the same as the ones from the shopping cart
        fail_message_product = "Product's info from the cart does not coincide with the info from the inventory page!"
        for i in range(len(product_info_from_inventory)):
            # print(self.compare_test_with_reference.__doc__)
            self.compare_test_with_reference(product_info_from_inventory[i], product_info_from_cart[i], fail_message_product)


    def test_continue_shopping_functionality(self):

        ## login with the predefined user (the credentials are declared as constants in the LoginPage class) 
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)

        ## add a product to the shopping cart
        InventoryPage.add_product_to_cart(self)

        ## go to the shopping cart
        self.click_element(self.CART_ICON_LOCATOR)

        ## verify that the "Continue Shopping" button returns the user to the landing/inventory page
        self.click_element(self.CONTINUE_SHOPPING_BUTTON_LOCATOR)

        fail_message_continue_shopping_button = "Inventory page was not successfully loaded after using the 'Continue shopping' button!"
        self.compare_test_with_reference(self.INVENTORY_PAGE_TITLE, LoginPage.get_landing_page_title(self), fail_message_continue_shopping_button)

