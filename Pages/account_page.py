from Pages.base_page import Basepage


class Accountpage(Basepage):

    def __inti__(self,Page):
        super().__init__(Page)

    news_letter_subscription_CSS ="//a[normalize-space()='Subscribe / unsubscribe to newsletter']"
    newsletter_subscription_yes_radio_checkbox_CSS = "//input[@value='1']"
    newsletter_subscription_no_radio_checkbox_CSS = "//input[@value='0']"

    def click_on_newsletter_subscription(self):
        self.click_on_element_basepage("news_letter_subscription_CSS",self.news_letter_subscription_CSS)

    def retrieving_newsletter_yes_radio_checkbox_value(self):
        return self.retreving_text_element_basepage("newsletter_subscription_yes_radio_checkbox_CSS",self.newsletter_subscription_yes_radio_checkbox_CSS)

    def retrieving_newsletter_no_radio_checkbox_value(self):
        return self.retreving_text_element_basepage("newsletter_subscription_no_radio_checkbox_CSS",self.newsletter_subscription_no_radio_checkbox_CSS)






