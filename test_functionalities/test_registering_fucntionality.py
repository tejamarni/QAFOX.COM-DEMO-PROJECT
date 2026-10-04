import allure
import pytest
from playwright.sync_api import expect
from Pages.home_page import HomePage
from test_functionalities.Base_test import TestBasetest
from utilities.excel_utility_file import update_case_result


class TestRegisteringFunctionality(TestBasetest):

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("testcaseid,first_name,last_name,email,telephone,password,confirm_password,news_letter_option,privacy_policy_checkbox_text",TestBasetest.get_excel_data(minrownumber=5,maxrownumber=7))
    def test_validate_registering_an_account_with_mandatory_fields(self, testcaseid, first_name,last_name,email,telephone,password,confirm_password,news_letter_option,privacy_policy_checkbox_text):
        homepage_obj = HomePage(self.page)
        registerpage_obj=homepage_obj.navigate_to_register_page()
        accountsuccess_page_obj=registerpage_obj.fill_all_registration_fields(first_name,last_name,
                                                      self.generating_email_with_timestamp(),telephone,
                                                      password,confirm_password,
                                                      news_letter_option,privacy_policy_checkbox_text)
        accountsuccess_text=accountsuccess_page_obj.retrieve_account_success_heading()
        actual_result = accountsuccess_text.inner_text()
        passed = "Your Account Has Been Created!" in actual_result
        update_case_result(
            self.cases_file, self.register_sheet,
            3 + int(testcaseid[-1]) - 1, actual_result, passed
        )
        self.expect(accountsuccess_text).to_have_text("Your Account Has Been Created!")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_validate_registering_an_account_without_providing_any_details(self):
        homepage_obj = HomePage(self.page)
        registerpage_obj=homepage_obj.navigate_to_register_page()
        registerpage_obj.click_on_continue_button()
        all_warning_texts=registerpage_obj.reterieving_all_warning_texts()
        all_warning_text_messages=registerpage_obj.reterieving_all_warning_texts()
        actual_result = "\n".join(
            warning_text.inner_text() for warning_text in all_warning_text_messages
        )
        update_case_result(
            self.cases_file, self.register_sheet, 6, actual_result, bool(actual_result)
        )
        for warning_text in all_warning_texts:
            self.expect(warning_text).to_have_text(all_warning_text_messages[all_warning_texts.index(warning_text)].inner_text())

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,first_name,last_name,email,"
                             "telephone,password,confirm_password,"
                             "news_letter_option,privacy_policy_checkbox_text",TestBasetest.get_excel_data(9,10))
    def test_validate_registering_an_account_with_newsletter_option(self, testcaseid,first_name,last_name,
                                                                                                   email,telephone,
                                                                                                   password,confirm_password,
                                                                                                   news_letter_option,privacy_policy_checkbox_text):
        homepage_obj = HomePage(self.page)
        registerpage_obj = homepage_obj.navigate_to_register_page()
        accountsuccess_page_obj = registerpage_obj.fill_all_registration_fields(first_name, last_name,
                                                                                self.generating_email_with_timestamp(),telephone,
                                                                                password, confirm_password,
                                                                                news_letter_option,privacy_policy_checkbox_text)
        accountsuccess_text = accountsuccess_page_obj.retrieve_account_success_heading()
        actual_result = accountsuccess_text.inner_text()
        passed = "Your Account Has Been Created!" in actual_result
        update_case_result(
            self.cases_file, self.register_sheet,
            int(testcaseid[-1]) + 2, actual_result, passed
        )
        self.expect(accountsuccess_text).to_have_text("Your Account Has Been Created!")
        accountpage_obj=accountsuccess_page_obj.click_on_continue_button()
        accountpage_obj.click_on_newsletter_subscription()
        if news_letter_option == "yes":
            checkbox=accountpage_obj.retrieving_newsletter_yes_radio_checkbox_value()
            self.expect(checkbox).to_be_checked()
        elif news_letter_option == "no":
            checkbox=accountpage_obj.retrieving_newsletter_no_radio_checkbox_value()
            self.expect(checkbox).to_be_checked()

    @allure.severity(allure.severity_level.NORMAL)
    def test_validate_different_ways_of_navigating_1_to_register_account(self):
        homepage_obj = HomePage(self.page)
        homepage_obj.navigate_to_register_page()
        actual_result = homepage_obj.retrieve_page_title()
        passed = actual_result == "Register Account"
        update_case_result(self.cases_file, self.register_sheet, 9, actual_result, passed)
        expect(self.page).to_have_title("Register Account")

    @allure.severity(allure.severity_level.NORMAL)
    def test_validate_different_ways_of_navigating_2_to_register_account(self):
        homepage_obj = HomePage(self.page)
        loginpage_obj=homepage_obj.navigate_to_login_page()
        loginpage_obj.navigate_to_register_page_with_continue_button()
        actual_result = homepage_obj.retrieve_page_title()
        passed = actual_result == "Register Account"
        update_case_result(self.cases_file, self.register_sheet, 9, actual_result, passed)
        expect(self.page).to_have_title("Register Account")

    @allure.severity(allure.severity_level.NORMAL)
    def test_validate_different_ways_of_navigating_3_to_register_account(self):
        homepage_obj = HomePage(self.page)
        loginpage_obj=homepage_obj.navigate_to_login_page()
        loginpage_obj.navigate_to_register_page_with_register_link()
        actual_result = homepage_obj.retrieve_page_title()
        passed = actual_result == "Register Account"
        update_case_result(self.cases_file, self.register_sheet, 9, actual_result, passed)
        expect(self.page).to_have_title("Register Account")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("testcaseid,first_name,last_name,"
                             "email,telephone,"
                             "password,confirm_password,"
                             "news_letter_option,privacy_policy_checkbox_text",TestBasetest.get_excel_data(minrownumber=11,maxrownumber=11))
    def test_validate_registering_an_account_by_entering_different_passwords(self,testcaseid,first_name,last_name,
                                                                             email,telephone,password,confirm_password,
                                                                             news_letter_option,privacy_policy_checkbox_text):
        homepage_obj = HomePage(self.page)
        registerpage_obj = homepage_obj.navigate_to_register_page()
        registerpage_obj.fill_all_registration_fields(first_name, last_name,
                                                      self.generating_email_with_timestamp(),telephone,
                                                      password, confirm_password,
                                                      news_letter_option, privacy_policy_checkbox_text)
        confirm_password_text=registerpage_obj.reterieving_confirm_password_warning_text()
        actual_result = confirm_password_text.inner_text()
        passed = "Password confirmation does not match password!" in actual_result
        update_case_result(self.cases_file, self.register_sheet, 10, actual_result, passed)
        expect(confirm_password_text).to_have_text("Password confirmation does not match password!")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("testcaseid,first_name,last_name,email,telephone,password,confirm_password,news_letter_option,privacy_policy_checkbox_text", TestBasetest.get_excel_data(minrownumber=12, maxrownumber=12))
    def test_validate_existing_email_address_warning_message(self,testcaseid, first_name, last_name, email, telephone, password, confirm_password, news_letter_option, privacy_policy_checkbox_text):
        homepage_obj = HomePage(self.page)
        registerpage_obj = homepage_obj.navigate_to_register_page()
        registerpage_obj.fill_all_registration_fields(first_name, last_name,
                                                      email, telephone,
                                                      password, confirm_password,
                                                      news_letter_option, privacy_policy_checkbox_text)
        existing_email_warning_text = registerpage_obj.reterieving_existing_email_warning_text()
        actual_result = existing_email_warning_text.inner_text()
        passed = "Warning: E-Mail Address is already registered!" in actual_result
        update_case_result(self.cases_file, self.register_sheet, 11, actual_result, passed)
        expect(existing_email_warning_text).to_have_text("Warning: E-Mail Address is already registered!")

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("testcaseid,first_name,last_name,email,telephone,password,confirm_password,news_letter_option,privacy_policy_checkbox_text", TestBasetest.get_excel_data(minrownumber=13, maxrownumber=13))
    def test_validating_to_checking_the_password_complexity_standards(self,testcaseid, first_name, last_name, email, telephone, password, confirm_password, news_letter_option, privacy_policy_checkbox_text):
        homepage_obj = HomePage(self.page)
        registerpage_obj = homepage_obj.navigate_to_register_page()
        registerpage_obj.fill_all_registration_fields(first_name, last_name,
                                                      self.generating_email_with_timestamp(), telephone,
                                                      password, confirm_password,
                                                      news_letter_option, privacy_policy_checkbox_text)
        password_warning_text = registerpage_obj.reterieving_password_complexity_warning_text()
        actual_result = password_warning_text.inner_text()
        passed = "Password must be between 4 and 20 characters!" in actual_result
        update_case_result(self.cases_file, self.register_sheet, 12, actual_result, passed)
        expect(password_warning_text).to_have_text("Password must be between 4 and 20 characters!")

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "testcaseid,first_name,last_name,email,telephone,password,confirm_password,news_letter_option,privacy_policy_checkbox_text",
        TestBasetest.get_excel_data(minrownumber=14, maxrownumber=14))
    def test_validating_to_register_without_accepting_privacy_policy(self, testcaseid, first_name, last_name, email,
                                                                      telephone, password, confirm_password,
                                                                      news_letter_option, privacy_policy_checkbox_text):
        homepage_obj = HomePage(self.page)
        registerpage_obj = homepage_obj.navigate_to_register_page()
        registerpage_obj.fill_all_registration_fields(first_name, last_name,
                                                      self.generating_email_with_timestamp(), telephone,
                                                      password, confirm_password,
                                                      news_letter_option, privacy_policy_checkbox_text)
        privacy_policy_checkbox_warning_text = registerpage_obj.reterieving_privacy_policy_checkbox_warning_text()
        actual_result = privacy_policy_checkbox_warning_text.inner_text()
        passed = "Warning: You must agree to the Privacy Policy!" in actual_result
        update_case_result(self.cases_file, self.register_sheet, 13, actual_result, passed)
        expect(privacy_policy_checkbox_warning_text).to_have_text("Warning: You must agree to the Privacy Policy!")
