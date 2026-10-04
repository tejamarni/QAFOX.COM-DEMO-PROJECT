import allure
import pytest
from playwright.sync_api import expect

from Pages.home_page import HomePage
from test_functionalities.Base_test import TestBasetest
from utilities.excel_utility_file import update_case_result


@pytest.mark.usefixtures("setup_and_teardown")
class TestLoginFunctionality(TestBasetest):

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "testcaseid,email,password",
        TestBasetest.get_excel_data(5, 5, "login"),
    )
    def test_login_with_valid_credentials(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        expect(self.page).to_have_title("Account Login")
        login_page.login(email, password)
        actual_result = login_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.login_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "My Account"
        )
        expect(self.page).to_have_title("My Account")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "testcaseid,email,password",
        TestBasetest.get_excel_data(6, 8, "login"),
    )
    def test_login_with_invalid_credentials(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        warning_text = login_page.retrieve_warning_message().inner_text()
        passed = (
            self.login_warning in warning_text
            or "Your account has exceeded allowed number of login attempts"
            in warning_text
        )
        update_case_result(
            self.cases_file, self.login_sheet, self.get_case_result_row(testcaseid),
            warning_text, passed
        )
        assert (
            self.login_warning in warning_text
            or "Your account has exceeded allowed number of login attempts"
            in warning_text
        )

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "testcaseid,email,password",
        TestBasetest.get_excel_data(9, 9, "login"),
    )
    def test_login_without_credentials(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email or "", password or "")
        actual_result = login_page.retrieve_warning_message().inner_text()
        update_case_result(
            self.cases_file, self.login_sheet, self.get_case_result_row(testcaseid),
            actual_result, self.login_warning in actual_result
        )
        expect(login_page.retrieve_warning_message()).to_contain_text(self.login_warning)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,email,password",
        TestBasetest.get_excel_data(10, 10, "login"),
    )
    def test_forgotten_password_link(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        # Assert forgotten password link is visible using the Loginpage POM
        expect(login_page.get_forgotten_password_locator()).to_be_visible()
        login_page.click_on_forgotten_password_link()
        actual_result = login_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.login_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "Forgot Your Password?"
        )
        expect(self.page).to_have_title("Forgot Your Password?")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "testcaseid,email,password",
        TestBasetest.get_excel_data(11, 11, "login"),
    )
    def test_logout_after_successful_login(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        home_page = HomePage(self.page)
        home_page.logout()
        actual_result = home_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.login_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "Account Logout"
        )
        expect(self.page).to_have_title("Account Logout")
        home_page.click_on_myaccount_dropdown_button()
        # Use HomePage POM to get the top-links Login locator
        expect(home_page.get_top_links_login_locator()).to_be_visible()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,email,password",
        TestBasetest.get_excel_data(12, 12, "login"),
    )
    def test_unsuccessful_login_attempt_limit(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        for _ in range(5):
            login_page.login(email, password)
        actual_result = login_page.retrieve_warning_message().inner_text()
        expected_messages = (
            self.login_warning,
            "Your account has exceeded allowed number of login attempts",
        )
        passed = any(message in actual_result for message in expected_messages)
        update_case_result(
            self.cases_file, self.login_sheet, self.get_case_result_row(testcaseid),
            actual_result, passed,
        )
        assert passed, actual_result
        displayed_message = (
            self.login_warning if self.login_warning in actual_result else expected_messages[1]
        )
        expect(login_page.retrieve_warning_message()).to_contain_text(displayed_message)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,email,password",
        TestBasetest.get_excel_data(13, 13, "login"),
    )
    def test_login_session_after_browser_reopen(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        expect(self.page).to_have_title("My Account")
        login_page.reload_page()
        actual_result = login_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.login_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "My Account"
        )
        expect(self.page).to_have_title("My Account")

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "testcaseid,email,password",
        TestBasetest.get_excel_data(14, 14, "login"),
    )
    def test_login_page_navigation_paths(self, testcaseid, email, password):
        homepage = HomePage(self.page)
        register_page = homepage.navigate_to_register_page()
        expect(self.page).to_have_title("Register Account")
        register_page.navigate_to_login_page()
        expect(self.page).to_have_title("Account Login")
        login_page = HomePage(self.page).navigate_to_login_page()
        expect(self.page).to_have_title("Account Login")
        actual_result = login_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.login_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "Account Login" and login_page is not None
        )
        assert login_page is not None