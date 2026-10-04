from datetime import datetime
from pathlib import Path

from playwright.sync_api import Page, expect

from Pages.add_to_cart_page import AddToCartPage
from utilities.excel_utility_file import (
    get_forgot_data_from_excel_file,
    get_add_to_cart_data_from_excel_file,
    get_checkout_data_from_excel_file,
    get_data_from_excel_file,
    get_login_data_from_excel_file,
    get_search_data_from_excel_file,
    update_case_result,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEST_DATA_FILE = PROJECT_ROOT / "TestData" / "test_data.xlsx"
CASES_FILE = PROJECT_ROOT / "Project Documents" / "QAFOX-Test_Cases.xlsx"


class TestBasetest:
    page = Page
    expect = expect
    cases_file = str(CASES_FILE)
    register_sheet = "Register"
    login_sheet = "Login"
    logout_sheet = "Logout"
    search_sheet = "Search"
    add_to_cart_sheet = "Add to Cart"
    checkout_sheet = "Checkout"
    demo_email = "qafoxdemoproject@gmail.com"
    demo_password = "@Github143"
    out_of_stock_warning = (
        "Products marked with *** are not available in the desired quantity or not in stock!"
    )
    search_no_results_text = (
        "There is no product that matches the search criteria"
    )
    login_warning = "Warning: No match for E-Mail Address and/or Password."
    forgot_password_sheet = "Forgot Password"
    forgot_password_success_text = (
        "An email with a confirmation link has been sent your email address."
    )
    forgot_password_warning_text = (
        "The E-Mail Address was not found in our records, please try again!"
    )

    def generating_email_with_timestamp(self):
        self.time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return "qafoxdemoid" + self.time_stamp + "@gmail.com"

    @staticmethod
    def get_case_result_row(testcaseid):
        return int(testcaseid.rsplit("_", 1)[1]) + 2

    def assert_and_record(self, testcaseid, actual_result, passed):
        update_case_result(
            self.cases_file,
            self.search_sheet,
            self.get_case_result_row(testcaseid),
            actual_result,
            passed,
        )
        assert passed, actual_result

    def record_add_to_cart_result(self, testcaseid, actual_result, passed):
        update_case_result(
            self.cases_file,
            self.add_to_cart_sheet,
            self.get_case_result_row(testcaseid),
            actual_result,
            passed,
        )
        assert passed, actual_result

    def record_checkout_result(self, testcaseid, actual_result, passed):
        update_case_result(
            self.cases_file,
            self.checkout_sheet,
            self.get_case_result_row(testcaseid),
            actual_result,
            passed,
        )
        assert passed, actual_result

    def verify_product_in_cart(self, testcaseid, product_name, use_header_cart=False):
        cart_page = AddToCartPage(self.page)
        success_message = cart_page.retrieve_success_message()
        message_passed = (
            "Success: You have added" in success_message
            and product_name in success_message
        )
        if not message_passed:
            self.record_add_to_cart_result(
                testcaseid,
                f"Expected add-to-cart success for '{product_name}', got: {success_message}",
                False,
            )

        if use_header_cart:
            cart_page.open_cart_from_header()
        else:
            cart_page.open_cart_from_success_message()

        cart_passed = cart_page.cart_contains_product(product_name)
        actual_result = (
            f"{success_message.strip()} "
            f"Product '{product_name}' present in Shopping Cart: {cart_passed}."
        )
        self.record_add_to_cart_result(
            testcaseid, actual_result, message_passed and cart_passed
        )

    @staticmethod
    def get_excel_data(minrownumber, maxrownumber, sheetname="register"):
        sheet = sheetname.lower()
        test_data_path = str(TEST_DATA_FILE)

        if sheet in ("login", "logout"):
            return get_login_data_from_excel_file(
                test_data_path,
                sheet,
                minrownum=minrownumber,
                maxrownum=maxrownumber,
            )

        return get_data_from_excel_file(
            test_data_path,
            sheetname,
            minrownum=minrownumber,
            maxrownum=maxrownumber,
        )

    @staticmethod
    def get_search_excel_data(minrownumber, maxrownumber):
        return get_search_data_from_excel_file(
            str(TEST_DATA_FILE),
            "search",
            minrownum=minrownumber,
            maxrownum=maxrownumber,
        )

    @staticmethod
    def get_add_to_cart_excel_data(minrownumber, maxrownumber):
        return get_add_to_cart_data_from_excel_file(
            str(TEST_DATA_FILE),
            "add_to_cart",
            minrownum=minrownumber,
            maxrownum=maxrownumber,
        )

    @staticmethod
    def get_checkout_excel_data(minrownumber, maxrownumber):
        return get_checkout_data_from_excel_file(
            str(TEST_DATA_FILE),
            "checkout",
            minrownum=minrownumber,
            maxrownum=maxrownumber,
        )

    @staticmethod
    def get_forgot_excel_data(minrownumber, maxrownumber):
        return get_forgot_data_from_excel_file(
            str(TEST_DATA_FILE),
            "forgot",
            minrownum=minrownumber,
            maxrownum=maxrownumber,
        )
