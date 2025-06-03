from selenium.webdriver.common.by import By
from setup.inventory_page import InventoryPage
from setup.login_page import LoginPage


class TestInventoryPage(InventoryPage, LoginPage):

    def test_az_default_sorting(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)

        in_app_sorting_option = self.get_text(self.SORT_DROPDOWN_CURRENT_LOCATOR)
        fail_message_sorting_default_option = f"The default sorting option should be: {self.DEFAULT_SORTING_OPTION}!"
        self.compare_test_with_reference(self.DEFAULT_SORTING_OPTION, in_app_sorting_option, fail_message_sorting_default_option)

        list_all_item_names_elements = self.find_elements(self.ITEMS_NAME_LOCATOR)
        list_all_item_names = []
        for element in list_all_item_names_elements:
            list_all_item_names.append(element.text)

        fail_message_elements_az_sorting = f"The default sorting option should be: {sorted(list_all_item_names)}!"
        self.compare_test_with_reference(sorted(list_all_item_names), list_all_item_names, fail_message_elements_az_sorting)

        self.assert_errors()


    def test_other_sorting(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)
        self.change_sorting_criteria()

        in_app_sorting_option = self.get_text(self.SORT_DROPDOWN_CURRENT_LOCATOR)
        if in_app_sorting_option == self.ZA_SORTING_OPTION:
            list_all_item_names_elements = self.find_elements(self.ITEMS_NAME_LOCATOR)
            list_all_item_names = []
            for element in list_all_item_names_elements:
                list_all_item_names.append(element.text)
            list_all_item_names_UI = list_all_item_names
            list_all_item_names.sort(reverse=True)

            fail_message_elements_za_sorting = f"The Z to A sorting option should be: {list_all_item_names}!"
            self.compare_test_with_reference(list_all_item_names, list_all_item_names_UI, fail_message_elements_za_sorting)

        elif in_app_sorting_option == self.LOHI_SORTING_OPTION:
            list_all_item_prices_elements = self.find_elements(self.ITEMS_PRICE_LOCATOR)
            list_all_item_prices = []
            for element in list_all_item_prices_elements:
                list_all_item_prices.append(float(element.text.strip('$')))
            list_all_item_prices_UI = list_all_item_prices
            list_all_item_prices.sort()

            fail_message_elements_lohi_sorting = f"The lowest to highest sorting option should be: {list_all_item_prices}!"
            self.compare_test_with_reference(list_all_item_prices, list_all_item_prices_UI, fail_message_elements_lohi_sorting)

        else:
            list_all_item_prices_elements = self.find_elements(self.ITEMS_PRICE_LOCATOR)
            list_all_item_prices = []
            for element in list_all_item_prices_elements:
                list_all_item_prices.append(float(element.text.strip('$')))
            list_all_item_prices_UI = list_all_item_prices
            list_all_item_prices.sort(reverse=True)

            fail_message_elements_hilo_sorting = f"The highest to lowest sorting option should be: {list_all_item_prices}!"
            self.compare_test_with_reference(list_all_item_prices, list_all_item_prices_UI, fail_message_elements_hilo_sorting)

        self.assert_errors()


    def test_product_added_to_cart(self):
        LoginPage.login_as_standard_user(self, LoginPage.USERNAME, LoginPage.PASSWORD)
        inventory_item = self.add_product_to_cart()

        fail_message_remove_button_displayed = "The 'Add to cart' button should have changed to 'Remove'!"
        self.compare_test_with_reference("Remove", self.driver.find_element(By.XPATH, f"{self.ADD_PRODUCT_TO_CART_LOCATOR_BY_XPATH}[{inventory_item}]").text, fail_message_remove_button_displayed)

        fail_message_cart_icon_update = "The cart icon should display a label of 1!"
        self.compare_test_with_reference(True, self.get_cart_icon_label(1), fail_message_cart_icon_update)

        self.assert_errors()
