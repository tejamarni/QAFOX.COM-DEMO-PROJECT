
from Pages.Loginpage import Loginpage
from Pages.base_page import Basepage
from Pages.forgot_password_page import ForgotPasswordPage
from Pages.register_page import Registerpage


class HomePage(Basepage):

    def __init__(self, Page):
        super().__init__(Page)

    my_account_dropdown_button_CSS = "a[title='My Account']"
    my_account_login_dropdown_button_CSS = "#top-links a:has-text('Login')"
    my_account_register_dropdown_button_CSS = "a:has-text('Register')"
    my_account_logout_dropdown_button_CSS = "#top-links a:has-text('Logout')"
    right_column_logout_link_CSS = "#column-right a:has-text('Logout')"
    right_column_login_link_CSS = "#column-right a:has-text('Login')"
    right_column_forgotten_password_link_CSS = "#column-right a:has-text('Forgotten Password')"

    def click_on_myaccount_dropdown_button(self):
        return self.click_on_element_basepage("my_account_dropdown_button_CSS", self.my_account_dropdown_button_CSS)

    def click_on_account_login_dropdown_button(self):
        self.click_on_element_basepage("my_account_login_dropdown_button_CSS", self.my_account_login_dropdown_button_CSS)
        return Loginpage(self.Page)

    def click_on_account_register_dropdown_button(self):
        self.click_on_element_basepage("my_account_register_dropdown_button_CSS", self.my_account_register_dropdown_button_CSS)
        return Registerpage(self.Page)

    def navigate_to_login_page(self):
        self.click_on_myaccount_dropdown_button()
        self.click_on_account_login_dropdown_button()
        return Loginpage(self.Page)

    def navigate_to_forgotten_password_from_right_column(self):
        self.click_on_element_basepage(
            "right_column_forgotten_password_link_CSS",
            self.right_column_forgotten_password_link_CSS,
        )
        return ForgotPasswordPage(self.Page)

    def navigate_to_register_page(self):
        self.click_on_myaccount_dropdown_button()
        self.click_on_account_register_dropdown_button()
        return Registerpage(self.Page)

    def logout(self):
        self.click_on_myaccount_dropdown_button()
        self.click_on_element_basepage(
            "my_account_logout_dropdown_button_CSS",
            self.my_account_logout_dropdown_button_CSS,
        )

    def logout_from_right_column(self):
        self.click_on_element_basepage(
            "right_column_logout_link_CSS", self.right_column_logout_link_CSS
        )

    def is_logout_visible_in_right_column(self):
        return self.Page.locator(self.right_column_logout_link_CSS).is_visible()

    def get_login_link_in_right_column(self):
        return self.get_element("right_column_login_link_CSS", self.right_column_login_link_CSS)

    def get_top_links_login_locator(self):
        """Return the Locator for the top-links Login link."""
        return self.get_element("my_account_login_dropdown_button_CSS", self.my_account_login_dropdown_button_CSS)
