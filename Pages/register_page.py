from Pages.account_success_page import AccountSuccessPage
from Pages.base_page import Basepage


class Registerpage(Basepage):

    def __init__(self,Page):
        super().__init__(Page)

    first_name_input_CSS = "#input-firstname"
    last_name_input_CSS = "#input-lastname"
    email_input_CSS = "#input-email"
    telephone_input_CSS = "#input-telephone"
    password_input_CSS = "#input-password"
    password_confirm_input_CSS = "#input-confirm"
    newsletter_yes_radio_button_CSS = "input[name='newsletter'][value='1']"
    newsletter_no_radio_button_CSS = "input[name='newsletter'][value='0']"
    privacy_policy_checkbox_CSS = "input[name='agree']"
    continue_button_CSS = "input[value='Continue']"
    first_name_warning_text_CSS = "//div[contains(text(),'First Name')]"
    last_name_warning_text_CSS = "//div[contains(text(),'Last Name')]"
    email_warning_text_CSS = "//div[contains(text(),'E-Mail Address')]"
    telephone_warning_text_CSS = "//div[contains(text(),'Telephone')]"
    password_warning_text_CSS = "//div[contains(text(),'Password')]"
    privacy_policy_checkbox_warning_text_CSS = "//div[contains(text(),'Warning: You must agree to the Privacy Policy!')]"
    confirm_password_warning_text_CSS = ".text-danger"
    existing_email_warning_text_CSS = "//div[contains(text(),'Warning: E-Mail Address is already registered!')]"
    login_page_link_CSS = "//a[normalize-space()='login page']"


    def fill_first_name(self,first_name):
        return self.element_fill_basepage("first_name_input_CSS", self.first_name_input_CSS,first_name)

    def fill_last_name(self,last_name):
        return self.element_fill_basepage("last_name_input_CSS", self.last_name_input_CSS,last_name)

    def fill_email(self,email):
        return self.element_fill_basepage("email_input_CSS", self.email_input_CSS,email)

    def fill_telephone(self,telephone):
        return self.element_fill_basepage("telephone_input_CSS", self.telephone_input_CSS,telephone)

    def fill_password(self,password):
        return self.element_fill_basepage("password_input_CSS", self.password_input_CSS,password)

    def fill_password_confirm(self,password_confirm):
        return self.element_fill_basepage("password_confirm_input_CSS", self.password_confirm_input_CSS,password_confirm)

    def click_on_newsletter_radio_button(self,radio_button_text):
        if radio_button_text.lower() == "yes":
            return self.click_on_element_basepage("newsletter_yes_radio_button_CSS", self.newsletter_yes_radio_button_CSS)
        elif radio_button_text.lower() == "no":
            return self.click_on_element_basepage("newsletter_no_radio_button_CSS", self.newsletter_no_radio_button_CSS)
        else:
            print("Choose any one of this YES/NO")

    def click_on_privacy_policy_checkbox(self,privacy_policy_checkbox_text):
        if privacy_policy_checkbox_text.lower() == "yes":
            return self.click_on_element_basepage("privacy_policy_checkbox_CSS", self.privacy_policy_checkbox_CSS)
        else:
            print("Choose YES to agree to the privacy policy")

    def click_on_continue_button(self):
        self.click_on_element_basepage("continue_button_CSS", self.continue_button_CSS)

    def fill_all_registration_fields(self, first_name, last_name, email, telephone, password, password_confirm,
                                     news_letter_option, privacy_policy_checkbox_text):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_telephone(telephone)
        self.fill_password(password)
        self.fill_password_confirm(password_confirm)
        self.click_on_newsletter_radio_button(news_letter_option)
        self.click_on_privacy_policy_checkbox(privacy_policy_checkbox_text)
        self.click_on_continue_button()
        return AccountSuccessPage(self.Page)

    def reterieving_all_warning_texts(self):
        first_name_warning_text=self.retreving_text_element_basepage("first_name_warning_text_CSS",self.first_name_warning_text_CSS)
        last_name_warning_text=self.retreving_text_element_basepage("last_name_warning_text_CSS",self.last_name_warning_text_CSS)
        email_warning_text=self.retreving_text_element_basepage("email_warning_text_CSS",self.email_warning_text_CSS)
        telephone_warning_text=self.retreving_text_element_basepage("telephone_warning_text_CSS",self.telephone_warning_text_CSS)
        password_warning_text=self.retreving_text_element_basepage("password_warning_text_CSS",self.password_warning_text_CSS)
        privacy_policy_checkbox_warning_text=self.retreving_text_element_basepage("privacy_policy_checkbox_warning_text_CSS",self.privacy_policy_checkbox_warning_text_CSS)
        return first_name_warning_text,last_name_warning_text,email_warning_text,telephone_warning_text,password_warning_text,privacy_policy_checkbox_warning_text

    def reterieving_confirm_password_warning_text(self):
        confirm_password_warning_text=self.retreving_text_element_basepage("confirm_password_warning_text_CSS",self.confirm_password_warning_text_CSS)
        return confirm_password_warning_text

    def reterieving_existing_email_warning_text(self):
        existing_email_warning_text=self.retreving_text_element_basepage("existing_email_warning_text_CSS",self.existing_email_warning_text_CSS)
        return existing_email_warning_text

    def reterieving_password_complexity_warning_text(self):
        password_warning_text=self.retreving_text_element_basepage("password_warning_text_CSS",self.password_warning_text_CSS)
        return password_warning_text

    def reterieving_privacy_policy_checkbox_warning_text(self):
        privacy_policy_checkbox_warning_text=self.retreving_text_element_basepage("privacy_policy_checkbox_warning_text_CSS",self.privacy_policy_checkbox_warning_text_CSS)
        return privacy_policy_checkbox_warning_text

    def navigate_to_login_page(self):
        from Pages.Loginpage import Loginpage

        self.click_on_element_basepage("login_page_link_CSS", self.login_page_link_CSS)
        return Loginpage(self.Page)


