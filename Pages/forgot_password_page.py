from Pages.base_page import Basepage


class ForgotPasswordPage(Basepage):
    email_input_CSS = "#input-email"
    continue_button_CSS = "input[value='Continue']"
    success_message_CSS = ".alert.alert-success"
    warning_message_CSS = ".alert.alert-danger"

    def enter_email(self, email):
        return self.element_fill_basepage(
            "email_input_CSS", self.email_input_CSS, email
        )

    def click_on_continue_button(self):
        return self.click_on_element_basepage(
            "continue_button_CSS", self.continue_button_CSS
        )

    def retrieve_success_message(self):
        return self.retreving_text_element_basepage(
            "success_message_CSS", self.success_message_CSS
        )

    def retrieve_warning_message(self):
        return self.retreving_text_element_basepage(
            "warning_message_CSS", self.warning_message_CSS
        )

    def is_success_message_visible(self):
        return self.get_element(
            "success_message_CSS", self.success_message_CSS
        ).count() > 0
