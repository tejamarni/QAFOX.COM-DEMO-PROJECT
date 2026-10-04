from Pages.Loginpage import Loginpage
from Pages.add_to_cart_page import AddToCartPage
from Pages.base_page import Basepage
from Pages.home_page import HomePage


class CheckoutPage(Basepage):
    header_checkout_link_CSS = "#top-links a[href*='route=checkout/checkout']"
    cart_checkout_link_CSS = "#content a.btn-primary[href*='route=checkout/checkout']"
    cart_continue_link_CSS = "#content a[href*='route=common/home']"
    page_heading_CSS = "#content h1"
    empty_cart_message_CSS = "#content p"
    cart_product_rows_CSS = "#content .table-responsive tbody tr"
    checkout_step_continue_button_CSS = "#button-payment-address"
    checkout_alert_CSS = "#checkout .alert, #content .alert"
    out_of_stock_warning = (
        "Products marked with *** are not available in the desired quantity or not in stock!"
    )

    def add_product_to_cart(self, product_name):
        cart_page = AddToCartPage(self.Page)
        cart_page.search_product(product_name)
        cart_page.add_product_from_search_results(product_name)
        cart_page.open_cart_from_success_message()

    def login(self, email, password):
        login_page = HomePage(self.Page).navigate_to_login_page()
        login_page.login(email, password)
        return Loginpage(self.Page)

    def open_checkout_from_header(self):
        self.Page.locator(self.header_checkout_link_CSS).click()

    def open_checkout_from_cart(self):
        self.Page.locator(self.cart_checkout_link_CSS).click()

    def continue_signed_in_checkout(self):
        button = self.Page.locator(self.checkout_step_continue_button_CSS)
        if button.is_visible():
            button.click()

    def heading(self):
        return self.Page.locator(self.page_heading_CSS).inner_text().strip()

    def is_checkout_page(self):
        return "route=checkout/checkout" in self.Page.url

    def is_cart_page(self):
        return "route=checkout/cart" in self.Page.url

    def is_cart_empty(self):
        return self.Page.locator(self.empty_cart_message_CSS).filter(
            has_text="Your shopping cart is empty!"
        ).count() > 0

    def cart_product_rows_text(self):
        return self.Page.locator(self.cart_product_rows_CSS).all_inner_texts()

    def has_unavailable_product_marker(self):
        return any("***" in row_text for row_text in self.cart_product_rows_text())

    def checkout_warning_text(self):
        alerts = self.Page.locator(self.checkout_alert_CSS).all_inner_texts()
        warning = " | ".join(text.strip() for text in alerts if text.strip())
        if warning:
            return warning
        if self.has_unavailable_product_marker():
            return self.out_of_stock_warning
        return ""

    def go_to_home_page(self):
        self.Page.locator(self.cart_continue_link_CSS).click()
