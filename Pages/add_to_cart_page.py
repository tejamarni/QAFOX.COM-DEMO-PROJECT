from Pages.base_page import Basepage


class AddToCartPage(Basepage):
    header_search_input_CSS = "#search input[name='search']"
    header_search_button_CSS = "#search button"
    product_cards_CSS = ".product-thumb"
    product_name_link_CSS = ".caption a"
    card_add_to_cart_button_CSS = "button[onclick*='cart.add']"
    product_page_add_to_cart_button_CSS = "#button-cart"
    related_products_CSS = "#content .product-thumb"
    success_alert_CSS = ".alert-success"
    cart_success_link_CSS = ".alert-success a[href*='checkout/cart']"
    header_cart_button_CSS = "#cart > button"
    header_cart_view_link_CSS = "#cart a[href*='checkout/cart']"
    cart_table_rows_CSS = "#content .table-responsive tbody tr"
    compare_button_CSS = "button[onclick*='compare.add']"
    comparison_page_add_to_cart_CSS = "input[value='Add to Cart']"
    category_mac_link_CSS = "#column-left a[href*='path=20_27']"
    desktops_menu_item_CSS = "#menu .nav > li"
    desktops_show_all_link_CSS = "#menu .dropdown-menu a[href$='path=20']"
    category_product_cards_CSS = ".product-thumb"
    featured_product_cards_CSS = "#content .product-thumb"
    product_comparison_link_CSS = "#compare-total"

    def search_product(self, product_name):
        self.element_fill_basepage(
            "header_search_input_CSS", self.header_search_input_CSS, product_name
        )
        self.click_on_element_basepage(
            "header_search_button_CSS", self.header_search_button_CSS
        )

    def open_first_search_result(self):
        self.Page.locator(self.product_cards_CSS).first.locator(
            self.product_name_link_CSS
        ).first.click()

    def add_product_from_search_results(self, product_name):
        card = self.Page.locator(self.product_cards_CSS).filter(
            has=self.Page.locator(self.product_name_link_CSS, has_text=product_name)
        ).first
        card.locator(self.card_add_to_cart_button_CSS).click()

    def add_product_from_product_page(self):
        self.click_on_element_basepage(
            "product_page_add_to_cart_button_CSS",
            self.product_page_add_to_cart_button_CSS,
        )

    def add_first_related_product(self):
        card = self.Page.locator(self.related_products_CSS).first
        product_name = card.locator(self.product_name_link_CSS).inner_text()
        card.locator(self.card_add_to_cart_button_CSS).click()
        return product_name.strip()

    def add_first_product_from_category(self):
        card = self.Page.locator(self.category_product_cards_CSS).first
        product_name = card.locator(self.product_name_link_CSS).inner_text()
        card.locator(self.card_add_to_cart_button_CSS).click()
        return product_name.strip()

    def navigate_to_mac_subcategory(self):
        self.Page.locator(self.category_mac_link_CSS).click()

    def navigate_to_desktops_category(self):
        self.Page.locator(self.desktops_menu_item_CSS).first.hover()
        self.Page.locator(self.desktops_show_all_link_CSS).click()

    def add_first_featured_product(self):
        card = self.Page.locator(self.featured_product_cards_CSS).first
        product_name = card.locator(self.product_name_link_CSS).inner_text()
        card.locator(self.card_add_to_cart_button_CSS).click()
        return product_name.strip()

    def add_product_to_comparison_from_search(self, product_name):
        card = self.Page.locator(self.product_cards_CSS).filter(
            has=self.Page.locator(self.product_name_link_CSS, has_text=product_name)
        ).first
        card.locator(self.compare_button_CSS).click()

    def open_product_comparison(self):
        self.Page.locator(self.product_comparison_link_CSS).click()

    def add_product_from_comparison(self):
        self.Page.locator(self.comparison_page_add_to_cart_CSS).click()

    def retrieve_success_message(self):
        return self.Page.locator(".alert").inner_text()

    def has_cart_success_message(self):
        return self.Page.locator(self.success_alert_CSS).count() > 0 and (
            "Success: You have added" in self.Page.locator(self.success_alert_CSS).inner_text()
        )

    def open_cart_from_success_message(self):
        self.Page.locator(self.cart_success_link_CSS).click()

    def open_cart_from_header(self):
        self.Page.locator(self.header_cart_button_CSS).click()
        self.Page.locator(self.header_cart_view_link_CSS).click()

    def cart_contains_product(self, product_name):
        return self.Page.locator(self.cart_table_rows_CSS).filter(
            has=self.Page.get_by_text(product_name, exact=True)
        ).count() > 0
