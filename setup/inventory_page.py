from random import randint
from setup.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):

    ## class constants
    DEFAULT_SORTING_OPTION = "Name (A to Z)"
    ZA_SORTING_OPTION = "Name (Z to A)"
    LOHI_SORTING_OPTION = "Price (low to high)"
    HILO_SORTING_OPTION = "Price (high to low)"

    ## class locators
    ITEMS_NAME_LOCATOR = (By.CLASS_NAME, "inventory_item_name")
    ITEMS_PRICE_LOCATOR = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, ".product_sort_container")
    SORT_DROPDOWN_CURRENT_LOCATOR = (By.CLASS_NAME, "active_option")
    ADD_PRODUCT_TO_CART_LOCATOR_BY_XPATH = "(//div[@class='inventory_list']//descendant::button)"
    CART_BADGE_LOCATOR = (By.CLASS_NAME, "shopping_cart_badge")


    ## class methods
    def change_sorting_criteria(self):
        """The "change_sorting_criteria" function can be run in two modes: with manual selection or with automated selection.
        If the "manual selection" code is the one not commented, then the test will require manual intervetion from a user to select which type of sorting should be applied.
        If the "automated selection" code is the one not commented, then the test will randomly select one of the available options for sorting.
        The type of sorting that was selected, either manually or automatically, is then applied.
        """

        ## manual selection:
        # user_input = (input("Alege tipul de sortare dorit: \n1. Name (A to Z)\n2. Name (Z to A)\n3. Price (low to high)\n4. Price (high to low)\n"))
        # while True:
        #     try:
        #         assert int(user_input) in range(1, 5)
        #     except:
        #         user_input = input("Doar urmatoarele optiuni sunt posibile (1, 2, 3 sau 4): \n1. Name (A to Z)\n2. Name (Z to A)\n3.Price (low to high)\n4. Price (high to low)\n")
        #     else:
        #         user_input = int(user_input)
        #         break

        ## automated selection:
        user_input = randint(1, 4)
        if user_input == 1:
            option_value = 'az'
        elif user_input == 2:
            option_value = 'za'
        elif user_input == 3:
            option_value = 'lohi'
        else:
            option_value = 'hilo'
        dropdown = Select(self.find_element(self.SORT_DROPDOWN_LOCATOR))
        dropdown.select_by_value(option_value)


    def add_product_to_cart(self):
        """The "add_product_to_cart" function can be run in two modes: with manual selection or with automated selection.
        If the "manual selection" code is the one not commented, then the test will require manual intervention from a user to select which product from the page should be added in the shopping cart.
        If the "automated selection" code is the one not commented, then the test will randomly select one of the available products on the page to be added in the shopping cart.
        The chosen product is added in the shopping cart.
        The function returns which product was added in the form of the variable user_input - out of all the available max_number products from the page, the one from the position user_input (0 < user_input <= max_number).
        """

        list_all_item_names_elements = self.find_elements(self.ITEMS_NAME_LOCATOR)
        max_number = len(list_all_item_names_elements)

        ## manual selection:
        # user_input = (input("Alege al catelea produs de pe pagina sa fie adaugat in cos!\n"))
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
        self.driver.find_element(By.XPATH, f"{self.ADD_PRODUCT_TO_CART_LOCATOR_BY_XPATH}[{user_input}]").click()
        return user_input


    def get_cart_icon_label(self, number):
        """The "get_cart_icon_label" function verifies if the label displayed next to the shopping cart coincides with the number entered as the function's parameter.
        If they do, the function returns True, otherwise, it returns False.
        """

        if int(self.get_text(self.CART_BADGE_LOCATOR)) == int(number):
            return True
        else:
            return False