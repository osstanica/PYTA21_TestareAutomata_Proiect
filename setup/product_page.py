from random import randint
from setup.base_page import BasePage
from selenium.webdriver.common.by import By
from setup.inventory_page import InventoryPage


class ProductPage(BasePage):

    ## class locators
    ITEM_NAME_LOCATOR_BY_XPATH = "(//div[@class='inventory_item_name '])"
    ITEM_DESCRIPTION_LOCATOR_BY_XPATH = "(//div[@class='inventory_item_desc'])"
    ITEM_PRICE_LOCATOR_BY_XPATH = "(//div[@class='inventory_item_price'])"
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, ".inventory_details_desc_container>.inventory_details_name")
    PRODUCT_DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, ".inventory_details_desc_container>.inventory_details_desc")
    PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, ".inventory_details_desc_container>.inventory_details_price")
    BACK_HOME_BUTTON_LOCATOR = (By.NAME, "back-to-products")

    ## class methods
    def get_inventory_product_details(self):
        """The "get_inventory_product_details" function can be run in two modes: with manual selection or with automated selection.
        If the "manual selection" code is the one not commented, then the test will require manual intervetion from a user to select for which product from the page should the details be returned.
        If the "automated selection" code is the one not commented, then the test will randomly select one of the available products on the page for which to return the details.
        The function returns which product was selected in the form of the variable user_input - out of all the available max_number products from the page, the one from the position user_input (0 < user_input <= max_number), the product name, product description and price.
        """

        list_all_item_names_elements = self.find_elements(InventoryPage.ITEMS_NAME_LOCATOR)
        max_number = len(list_all_item_names_elements)
        ## manual selection:
        # user_input = (input("Alege al catelea produs de pe pagina sa fie vizualizat!\n"))
        # while True:
        #     try:
        #         assert int(user_input) in range(1, max_number+1)
        #     except:
        #         user_input = input(f"Sunt maxim {max_number} produse pe pagina. Al catelea sa fie?\n")
        #     else:
        #         user_input = int(user_input)
        #         break

        ## automated selection:
        user_input = randint(1, max_number)
        product_name = self.driver.find_element(By.XPATH, f"{self.ITEM_NAME_LOCATOR_BY_XPATH}[{user_input}]").text
        product_description = self.driver.find_element(By.XPATH, f"{self.ITEM_DESCRIPTION_LOCATOR_BY_XPATH}[{user_input}]").text
        product_price = self.driver.find_element(By.XPATH, f"{self.ITEM_PRICE_LOCATOR_BY_XPATH}[{user_input}]").text.strip('$')

        return user_input, product_name, product_description, product_price