from Pages.base_page import Basepage


class SearchPage(Basepage):
    header_search_input_CSS = "#search input[name='search']"
    header_search_button_CSS = "#search button"
    search_criteria_input_CSS = "#input-search"
    category_dropdown_CSS = "select[name='category_id']"
    subcategory_checkbox_CSS = "input[name='sub_category']"
    search_form_button_CSS = "#button-search"
    product_card_CSS = ".product-thumb"
    product_view_controls_CSS = ".button-group button"
    product_name_link_CSS = ".caption a"
    no_results_message_CSS = "#content p:has-text('There is no product that matches the search criteria')"
    list_view_button_CSS = "#list-view"
    grid_view_button_CSS = "#grid-view"
    list_view_container_CSS = ".product-list"
    sort_dropdown_CSS = "#input-sort"
    page_heading_CSS = "#content h1"

    def search_from_header(self, search_term=""):
        self.element_fill_basepage(
            "header_search_input_CSS", self.header_search_input_CSS, search_term
        )
        self.click_on_element_basepage(
            "header_search_button_CSS", self.header_search_button_CSS
        )

    def search_from_search_page(
        self, search_term, category_label=None, include_subcategories=False
    ):
        self.element_fill_basepage(
            "search_criteria_input_CSS", self.search_criteria_input_CSS, search_term
        )
        if category_label is not None:
            category_dropdown = self.Page.locator(self.category_dropdown_CSS)
            category_value = next(
                option.get_attribute("value")
                for option in category_dropdown.locator("option").all()
                if (option.inner_text() or "").strip() == category_label
            )
            category_dropdown.select_option(value=category_value)
        checkbox = self.Page.locator(self.subcategory_checkbox_CSS)
        if include_subcategories and not checkbox.is_checked():
            checkbox.check()
        elif not include_subcategories and checkbox.is_checked():
            checkbox.uncheck()
        self.click_on_element_basepage(
            "search_form_button_CSS", self.search_form_button_CSS
        )

    def products(self):
        return self.Page.locator(self.product_card_CSS)

    def no_results_message(self):
        return self.Page.locator(self.no_results_message_CSS)

    def select_list_view(self):
        self.click_on_element_basepage("list_view_button_CSS", self.list_view_button_CSS)

    def select_grid_view(self):
        self.click_on_element_basepage("grid_view_button_CSS", self.grid_view_button_CSS)

    def select_sort_option(self, option_text):
        self.Page.locator(self.sort_dropdown_CSS).select_option(label=option_text)

    def product_view_controls_count(self):
        return self.products().first.locator(self.product_view_controls_CSS).count()

    def is_list_view_visible(self):
        return self.Page.locator(self.list_view_container_CSS).count() > 0

    def open_first_product_and_return_heading(self):
        self.products().first.locator(self.product_name_link_CSS).first.click()
        heading = self.Page.locator(self.page_heading_CSS).inner_text()
        self.Page.go_back()
        return heading

    def selected_sort_value(self):
        return self.Page.locator(self.sort_dropdown_CSS).input_value()

    def page_heading(self):
        return self.Page.locator(self.page_heading_CSS).inner_text()

    def open_sitemap_search(self):
        self.Page.locator("footer a[href*='route=information/sitemap']").click()
        self.Page.locator("#content a[href*='route=product/search']").click()
