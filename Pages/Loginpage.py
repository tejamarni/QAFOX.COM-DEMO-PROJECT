from Pages.base_page import Basepage
from Pages.forgot_password_page import ForgotPasswordPage
from Pages.register_page import Registerpage


class Loginpage(Basepage):
    def __init__(self,Page):
        super().__init__(Page)

    continue_button_for_register_page_CSS = "a[class='btn btn-primary']"
    registerpage_link_CSS = "//a[@class='list-group-item'][normalize-space()='Register']"
    email_input_CSS = "#input-email"
    password_input_CSS = "#input-password"
    login_button_CSS = "input[value='Login']"
    forgotten_password_link_CSS = "#content a:has-text('Forgotten Password')"
    warning_message_CSS = ".alert.alert-danger"

    def navigate_to_register_page_with_continue_button(self):
        self.click_on_element_basepage("continue_button_for_register_page_CSS",self.continue_button_for_register_page_CSS)
        return Registerpage(self.Page)

    def navigate_to_register_page_with_register_link(self):
        self.click_on_element_basepage("registerpage_link_CSS",self.registerpage_link_CSS)
        return Registerpage(self.Page)

    def login(self, email="", password=""):
        self.element_fill_basepage("email_input_CSS", self.email_input_CSS, email)
        self.element_fill_basepage("password_input_CSS", self.password_input_CSS, password)
        self.click_on_element_basepage("login_button_CSS", self.login_button_CSS)

    def click_on_forgotten_password_link(self):
        self.click_on_element_basepage(
            "forgotten_password_link_CSS", self.forgotten_password_link_CSS
        )
        return ForgotPasswordPage(self.Page)

    def retrieve_warning_message(self):
        return self.retreving_text_element_basepage(
            "warning_message_CSS", self.warning_message_CSS
        )

    def get_forgotten_password_locator(self):
        """Return the Locator for the forgotten password link so tests can assert visibility or click."""
        return self.get_element("forgotten_password_link_CSS", self.forgotten_password_link_CSS)

    def is_login_visible_in_top_menu(self):
        return self.Page.locator("#top-links a:has-text('Login')").is_visible()
