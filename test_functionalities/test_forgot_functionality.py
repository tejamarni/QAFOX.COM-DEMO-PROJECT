import allure
import pytest
from playwright.sync_api import expect

from Pages.home_page import HomePage
from test_functionalities.Base_test import TestBasetest
from utilities.excel_utility_file import update_case_result

class TestForgotFunctionality(TestBasetest):

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("testcaseid,email", TestBasetest.get_forgot_excel_data(5, 5))
    def test_reset_password_for_registered_email(self, testcaseid, email):
        forgot_page = HomePage(self.page).navigate_to_login_page().click_on_forgotten_password_link()
        expect(self.page).to_have_title("Forgot Your Password?")
        forgot_page.enter_email(email)
        forgot_page.click_on_continue_button()
        actual = forgot_page.retrieve_success_message().inner_text()
        passed = self.forgot_password_success_text in actual
        update_case_result(self.cases_file, self.forgot_password_sheet, 3, actual, passed)
        assert passed, actual

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,email", TestBasetest.get_forgot_excel_data(6, 6))
    def test_reset_password_email_confirmation_ui(self, testcaseid, email):
        forgot_page = HomePage(self.page).navigate_to_login_page().click_on_forgotten_password_link()
        forgot_page.enter_email(email)
        forgot_page.click_on_continue_button()
        actual = forgot_page.retrieve_success_message().inner_text()
        passed = self.forgot_password_success_text in actual
        update_case_result(
            self.cases_file,
            self.forgot_password_sheet,
            4,
            actual + " Email inbox verification is outside browser scope.",
            passed,
        )
        assert passed, actual

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("testcaseid,email", TestBasetest.get_forgot_excel_data(7, 7))
    def test_reset_password_for_non_registered_email(self, testcaseid, email):
        forgot_page = HomePage(self.page).navigate_to_login_page().click_on_forgotten_password_link()
        forgot_page.enter_email(email)
        forgot_page.click_on_continue_button()
        actual = (
            forgot_page.retrieve_success_message().inner_text()
            if forgot_page.is_success_message_visible()
            else forgot_page.retrieve_warning_message().inner_text()
        )
        passed = self.forgot_password_warning_text in actual
        update_case_result(
            self.cases_file,
            self.forgot_password_sheet,
            5,
            actual + " Prepared data contains a registered email; site returned its actual response.",
            passed,
        )
        assert passed, actual

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,email_values", TestBasetest.get_forgot_excel_data(8, 8))
    def test_invalid_email_formats(self, testcaseid, email_values):
        forgot_page = HomePage(self.page).navigate_to_login_page().click_on_forgotten_password_link()
        results = []
        for email in email_values.splitlines():
            email = email.split(")", 1)[-1].strip()
            forgot_page.enter_email(email)
            forgot_page.click_on_continue_button()
            results.append(f"{email}: {forgot_page.retrieve_warning_message().inner_text()}")
            forgot_page = HomePage(self.page).navigate_to_login_page().click_on_forgotten_password_link()
        passed = all(self.forgot_password_warning_text in result for result in results)
        update_case_result(
            self.cases_file,
            self.forgot_password_sheet,
            6,
            "\n".join(results),
            passed,
        )
        assert passed, "\n".join(results)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,email", TestBasetest.get_forgot_excel_data(9, 9))
    def test_forgot_password_from_right_column(self, testcaseid, email):
        homepage = HomePage(self.page)
        homepage.click_on_myaccount_dropdown_button()
        homepage.click_on_account_login_dropdown_button()
        homepage.navigate_to_forgotten_password_from_right_column()
        expect(self.page).to_have_title("Forgot Your Password?")
        update_case_result(
            self.cases_file,
            self.forgot_password_sheet,
            7,
            "Forgot Your Password page displayed from Right Column.",
            True,
        )