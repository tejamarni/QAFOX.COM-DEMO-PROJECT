import allure
import pytest

from Pages.checkout_page import CheckoutPage
from test_functionalities.Base_test import TestBasetest


class TestCheckoutFunctionality(TestBasetest):

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_checkout_excel_data(5, 5),
    )
    def test_checkout_header_with_empty_cart(self, testcaseid, product_name):
        checkout_page = CheckoutPage(self.page)
        checkout_page.open_checkout_from_header()
        is_empty_cart = checkout_page.is_cart_page() and checkout_page.is_cart_empty()
        actual_result = (
            f"Checkout navigation landed on '{checkout_page.heading()}'; "
            f"empty cart message displayed: {checkout_page.is_cart_empty()}."
        )
        self.record_checkout_result(testcaseid, actual_result, is_empty_cart)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_checkout_excel_data(6, 6),
    )
    def test_checkout_from_shopping_cart(self, testcaseid, product_name):
        checkout_page = CheckoutPage(self.page)
        checkout_page.add_product_to_cart(product_name)
        checkout_page.open_checkout_from_cart()
        reached_checkout = checkout_page.is_checkout_page()
        unavailable = checkout_page.has_unavailable_product_marker()
        warning = checkout_page.checkout_warning_text()
        passed = not reached_checkout and unavailable and self.out_of_stock_warning in warning
        actual_result = (
            f"Checkout URL reached: {reached_checkout}; current page "
            f"'{checkout_page.heading()}'; product unavailable marker: {unavailable}; "
            f"warning: {warning or 'none'}."
        )
        self.record_checkout_result(testcaseid, actual_result, passed)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_checkout_excel_data(7, 7),
    )
    def test_checkout_using_header_after_adding_product(self, testcaseid, product_name):
        checkout_page = CheckoutPage(self.page)
        checkout_page.add_product_to_cart(product_name)
        checkout_page.open_checkout_from_header()
        reached_checkout = checkout_page.is_checkout_page()
        unavailable = checkout_page.has_unavailable_product_marker()
        warning = checkout_page.checkout_warning_text()
        passed = not reached_checkout and unavailable and self.out_of_stock_warning in warning
        actual_result = (
            f"Header Checkout reached checkout URL: {reached_checkout}; current page "
            f"'{checkout_page.heading()}'; product unavailable marker: {unavailable}; "
            f"warning: {warning or 'none'}."
        )
        self.record_checkout_result(testcaseid, actual_result, passed)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_checkout_excel_data(8, 8),
    )
    def test_signed_in_checkout_using_existing_address(self, testcaseid, product_name):
        checkout_page = CheckoutPage(self.page)
        checkout_page.login(self.demo_email, self.demo_password)
        checkout_page.add_product_to_cart(product_name)
        checkout_page.open_checkout_from_cart()
        reached_checkout = checkout_page.is_checkout_page()
        unavailable = checkout_page.has_unavailable_product_marker()
        warning = checkout_page.checkout_warning_text()
        if reached_checkout:
            checkout_page.continue_signed_in_checkout()
            warning = checkout_page.checkout_warning_text()
            unavailable = unavailable or self.out_of_stock_warning in warning
        passed = (
            not reached_checkout and unavailable and self.out_of_stock_warning in warning
        ) or (reached_checkout and self.out_of_stock_warning in warning)
        actual_result = (
            f"Signed-in checkout page reached: {reached_checkout}; "
            f"unavailable item marker: {unavailable}; checkout warning: "
            f"{warning or 'none'}."
        )
        self.record_checkout_result(testcaseid, actual_result, passed)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "testcaseid,product_name",
        TestBasetest.get_checkout_excel_data(9, 9),
    )
    def test_guest_checkout(self, testcaseid, product_name):
        checkout_page = CheckoutPage(self.page)
        checkout_page.add_product_to_cart(product_name)
        checkout_page.open_checkout_from_cart()
        reached_checkout = checkout_page.is_checkout_page()
        unavailable = checkout_page.has_unavailable_product_marker()
        warning = checkout_page.checkout_warning_text()
        passed = not reached_checkout and unavailable and self.out_of_stock_warning in warning
        actual_result = (
            f"Guest checkout page reached: {reached_checkout}; current page "
            f"'{checkout_page.heading()}'; unavailable item marker: {unavailable}; "
            f"warning: {warning or 'none'}."
        )
        self.record_checkout_result(testcaseid, actual_result, passed)