from setup.base_page import BasePage
from setup.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):

    ## class variables
    DEFAULT_SORTING_OPTION = "Name (A to Z)"
    ZA_SORTING_OPTION = "Name (Z to A)"
    LOHI_SORTING_OPTION = "Price (low to high)"
    HILO_SORTING_OPTION = "Price (high to low)"

    ## class locators
    ITEMS_NAME_LOCATOR = (By.CLASS_NAME, "inventory_item_name ")
    ITEMS_PRICE_LOCATOR = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, ".product_sort_container")
    SORT_DROPDOWN_CURRENT_LOCATOR = (By.CLASS_NAME, "active_option")
    ADD_PRODUCT_TO_CART_LOCATOR_By_XPATH = "//div[@class='inventory_list']//descendant::button"
    CART_ICON_LOCATOR = (By.CLASS_NAME, "shopping_cart_badge")

    ## class methods
    def change_sorting_criteria(self):
        user_input = (input("Alege tipul de sortare dorit: \n1. Name (A to Z)\n2. Name (Z to A)\n3. Price (low to high)\n4. Price (high to low)\n"))
        while True:
            try:
                assert int(user_input) in range(1, 5)
            except:
                user_input = input("Doar urmatoarele optiuni sunt posibile (1, 2, 3 sau 4): \n1. Name (A to Z)\n2. Name (Z to A)\n3.Price (low to high)\n4. Price (high to low)\n")
            else:
                user_input = int(user_input)
                break
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
        list_all_item_names_elements = self.find_elements(self.ITEMS_NAME_LOCATOR)
        max_number = len(list_all_item_names_elements)
        user_input = (input("Alege al catelea produs de pe pagina sa fie adaugat in cos!\n"))
        while True:
            try:
                assert int(user_input) in range(1, max_number+1)
            except:
                user_input = input(f"Sunt maxim {max_number} produse pe pagina. Al catelea sa fie?\n")
            else:
                user_input = int(user_input)
                break

        self.driver.find_element(By.XPATH, f"({self.ADD_PRODUCT_TO_CART_LOCATOR_By_XPATH})[{user_input}]").click()
        return user_input


    def get_cart_icon_label(self, number):
        if int(self.get_text(self.CART_ICON_LOCATOR)) == int(number):
            return True
        else:
            return False