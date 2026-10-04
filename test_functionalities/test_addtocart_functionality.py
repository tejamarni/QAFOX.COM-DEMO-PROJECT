import allure
import pytest

from Pages.add_to_cart_page import AddToCartPage
from test_functionalities.Base_test import TestBasetest


class TestAddToCartFunctionality(TestBasetest):

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_add_to_cart_excel_data(5, 5),
    )
    def test_add_to_cart_from_product_display_page(self, testcaseid, product_name):
        add_to_cart_page = AddToCartPage(self.page)
        add_to_cart_page.search_product(product_name)
        add_to_cart_page.open_first_search_result()
        add_to_cart_page.add_product_from_product_page()
        self.verify_product_in_cart(testcaseid, product_name)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_add_to_cart_excel_data(6, 6),
    )
    def test_add_to_cart_from_search_results(self, testcaseid, product_name):
        add_to_cart_page = AddToCartPage(self.page)
        add_to_cart_page.search_product(product_name)
        add_to_cart_page.add_product_from_search_results(product_name)
        self.verify_product_in_cart(
            testcaseid, product_name, use_header_cart=True
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_add_to_cart_excel_data(7, 7),
    )
    def test_add_to_cart_from_category_page(self, testcaseid, product_name):
        add_to_cart_page = AddToCartPage(self.page)
        add_to_cart_page.navigate_to_desktops_category()
        add_to_cart_page.navigate_to_mac_subcategory()
        added_product_name = add_to_cart_page.add_first_product_from_category()
        self.verify_product_in_cart(testcaseid, added_product_name)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_add_to_cart_excel_data(8, 8),
    )
    def test_add_to_cart_from_featured_products(self, testcaseid, product_name):
        add_to_cart_page = AddToCartPage(self.page)
        added_product_name = add_to_cart_page.add_first_featured_product()
        self.verify_product_in_cart(testcaseid, added_product_name)