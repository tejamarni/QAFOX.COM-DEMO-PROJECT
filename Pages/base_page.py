

class Basepage:
    def __init__(self, Page):
        self.Page = Page

    def retrieve_page_title(self):
        return self.Page.title()

    def navigate_back(self):
        return self.Page.go_back()

    def reload_page(self):
        return self.Page.reload()

    def click_on_element_basepage(self,locator_text,locator_value):
        element = self.get_element(locator_text,locator_value)
        return element.click()

    def click_on_element(self,locator_text,locator_value):
        element = self.get_element(locator_text,locator_value)
        return element.click()

    def element_fill_basepage(self,locator_text,locator_value,product_text):
        element = self.get_element(locator_text,locator_value)
        element.click()
        return element.fill(product_text)

    def retreving_text_element_basepage(self,locator_text,locator_value):
        element = self.get_element(locator_text,locator_value)
        return element


    def get_element(self,locator_text,locator_value):
        element = None
        if locator_text.endswith("_CSS"):
            element = self.Page.locator(f"{locator_value}")
        elif locator_text.endswith("_LABLE"):
            element = self.Page.get_by_label(locator_value)
        elif locator_text.endswith("_PLACEHOLDER"):
            element = self.Page.get_by_placeholder(locator_value)
        elif locator_text.endswith("_TEXT"):
            element = self.Page.get_by_text(locator_value)
        elif locator_text.endswith("_ROLE"):
            element = self.Page.get_by_role(locator_value)
        elif locator_text.endswith("_ALT_TEXT"):
            element = self.Page.get_by_alt_text(locator_value)
        return element








