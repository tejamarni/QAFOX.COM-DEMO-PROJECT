import allure
import pytest
from playwright.sync_api import expect

from Pages.home_page import HomePage
from test_functionalities.Base_test import TestBasetest
from Pages.account_success_page import AccountSuccessPage
from utilities.excel_utility_file import update_case_result


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogoutFunctionality(TestBasetest):

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("testcaseid,email,password", TestBasetest.get_excel_data(5, 5, "logout"))
    def test_logout_from_my_account_menu(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        home_page = HomePage(self.page)
        home_page.logout()
        expect(self.page).to_have_title("Account Logout")
        # use POM helper to get the login link locator in right column
        expect(home_page.get_login_link_in_right_column()).to_be_visible()
        # click the Continue button via AccountSuccessPage POM
        AccountSuccessPage(self.page).click_on_continue_button()
        actual_result = home_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.logout_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "Your Store"
        )
        expect(self.page).to_have_title("Your Store")

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("testcaseid,email,password", TestBasetest.get_excel_data(6, 6, "logout"))
    def test_logout_from_right_column(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        HomePage(self.page).logout_from_right_column()
        actual_result = HomePage(self.page).retrieve_page_title()
        update_case_result(
            self.cases_file, self.logout_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "Account Logout"
        )
        expect(self.page).to_have_title("Account Logout")
        expect(HomePage(self.page).get_login_link_in_right_column()).to_be_visible()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,email,password", TestBasetest.get_excel_data(7, 7, "logout"))
    def test_session_is_maintained_after_page_reopen(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        expect(self.page).to_have_title("My Account")
        login_page.reload_page()
        actual_result = login_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.logout_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "My Account"
        )
        expect(self.page).to_have_title("My Account")

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,email,password", TestBasetest.get_excel_data(8, 8, "logout"))
    def test_browser_back_after_logout_does_not_restore_session(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        HomePage(self.page).logout()
        login_page.navigate_back()
        login_page.reload_page()
        actual_result = login_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.logout_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "Account Logout"
        )
        expect(HomePage(self.page).get_login_link_in_right_column()).to_be_visible()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,email,password", TestBasetest.get_excel_data(9, 9, "logout"))
    def test_logout_is_not_visible_before_login(self, testcaseid, email, password):
        homepage = HomePage(self.page)
        homepage.click_on_myaccount_dropdown_button()
        homepage.click_on_account_register_dropdown_button()
        actual_result = homepage.retrieve_page_title()
        update_case_result(
            self.cases_file, self.logout_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "Register Account" and not homepage.is_logout_visible_in_right_column()
        )
        expect(self.page).to_have_title("Register Account")
        assert not homepage.is_logout_visible_in_right_column()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,email,password", TestBasetest.get_excel_data(10, 10, "logout"))
    def test_login_again_immediately_after_logout(self, testcaseid, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        HomePage(self.page).logout()
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email, password)
        actual_result = login_page.retrieve_page_title()
        update_case_result(
            self.cases_file, self.logout_sheet, self.get_case_result_row(testcaseid),
            actual_result, actual_result == "My Account"
        )
        expect(self.page).to_have_title("My Account")