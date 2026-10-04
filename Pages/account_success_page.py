from Pages.account_page import Accountpage
from Pages.base_page import Basepage


class AccountSuccessPage(Basepage):

    def __init__(self, Page):
        super().__init__(Page)

    account_success_heading_CSS = "div#content h1"
    continue_button_CSS = "//a[normalize-space()='Continue']"

    def retrieve_account_success_heading(self):
        element = self.get_element("account_success_heading_CSS", self.account_success_heading_CSS)
        return element

    def click_on_continue_button(self):
        self.click_on_element_basepage("continue_button_CSS",self.continue_button_CSS)
        return Accountpage(self.Page)
