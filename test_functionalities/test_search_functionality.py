import allure
import pytest

from Pages.home_page import HomePage
from Pages.search_page import SearchPage
from test_functionalities.Base_test import TestBasetest


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearchFunctionality(TestBasetest):

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(5, 5), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_search_existing_product(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.search_from_header(product)
        count = search_page.products().count()
        self.assert_and_record(
            testcaseid,
            f"Search '{product}' displayed {count} matching product card(s).",
            count > 0,
        )

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(6, 6), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_search_non_existing_product(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.search_from_header(product)
        message = search_page.no_results_message().inner_text()
        self.assert_and_record(
            testcaseid, message, self.search_no_results_text in message
        )

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(7, 7), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_search_without_product_name(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.search_from_header()
        message = search_page.no_results_message().inner_text()
        self.assert_and_record(
            testcaseid, message, self.search_no_results_text in message
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(8, 8), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_search_product_after_login(self, testcaseid, product, category, email, password):
        login_page = HomePage(self.page).navigate_to_login_page()
        login_page.login(email.strip(), password.strip())
        search_page = SearchPage(self.page)
        search_page.search_from_header(product)
        count = search_page.products().count()
        self.assert_and_record(
            testcaseid,
            f"After login, search '{product}' displayed {count} product(s).",
            count > 0,
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(9, 9), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_search_criteria_matching_multiple_products(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.search_from_header(product)
        count = search_page.products().count()
        self.assert_and_record(
            testcaseid,
            f"Search '{product}' displayed {count} matching product(s).",
            count > 1,
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,product,categories,email,password", TestBasetest.get_search_excel_data(10, 10), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_search_using_product_category(self, testcaseid, product, categories, email, password):
        correct_category, wrong_category = [
            value.split(":", 1)[1].strip() for value in categories.splitlines()
        ]
        search_page = SearchPage(self.page)
        search_page.search_from_header()
        search_page.search_from_search_page(product, category_label=correct_category)
        correct_count = search_page.products().count()
        search_page.search_from_search_page(product, category_label=wrong_category)
        wrong_message = search_page.no_results_message().inner_text()
        passed = correct_count > 0 and self.search_no_results_text in wrong_message
        self.assert_and_record(
            testcaseid,
            f"Category '{correct_category}' returned {correct_count} product(s); "
            f"category '{wrong_category}' returned: {wrong_message}",
            passed,
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(11, 11), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_search_in_subcategories(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.search_from_header()
        search_page.search_from_search_page(product, category_label=category)
        parent_count = search_page.products().count()
        search_page.search_from_search_page(
            product, category_label=category, include_subcategories=True
        )
        subcategory_count = search_page.products().count()
        passed = parent_count == 0 and subcategory_count > 0
        self.assert_and_record(
            testcaseid,
            f"Parent category returned {parent_count} products; including "
            f"subcategories returned {subcategory_count}.",
            passed,
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(12, 12), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_list_and_grid_views_for_single_product(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.search_from_header(product)
        single_result = search_page.products().count() == 1
        options_visible = search_page.product_view_controls_count() >= 2
        search_page.select_list_view()
        list_view = search_page.is_list_view_visible()
        opened_product = search_page.open_first_product_and_return_heading()
        search_page.select_grid_view()
        grid_view = search_page.products().count() == 1
        passed = (
            single_result
            and options_visible
            and list_view
            and opened_product == product
            and grid_view
        )
        self.assert_and_record(
            testcaseid,
            f"Single result={single_result}; controls visible={options_visible}; "
            f"list view={list_view}; opened product='{opened_product}'; "
            f"grid view={grid_view}.",
            passed,
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(13, 13), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_list_and_grid_views_for_multiple_products(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.search_from_header(product)
        result_count = search_page.products().count()
        search_page.select_list_view()
        list_view_count = search_page.products().count()
        search_page.select_grid_view()
        grid_view_count = search_page.products().count()
        passed = (
                1 < result_count == list_view_count
                and grid_view_count == result_count
        )
        self.assert_and_record(
            testcaseid,
            f"Search displayed {result_count}; list view displayed {list_view_count}; "
            f"grid view displayed {grid_view_count}.",
            passed,
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(14, 14), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_sort_search_results(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.search_from_header(product)
        result_count = search_page.products().count()
        sort_options = ["Name (A - Z)", "Price (Low > High)", "Rating (Highest)"]
        selections = []
        for option in sort_options:
            search_page.select_sort_option(option)
            selections.append(search_page.selected_sort_value())
        passed = result_count > 1 and all(selections)
        self.assert_and_record(
            testcaseid,
            f"{result_count} products found; selected sort values: {selections}.",
            passed,
        )

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("testcaseid,product,category,email,password", TestBasetest.get_search_excel_data(15, 15), ids=lambda value: value if isinstance(value, str) and value.startswith("TC_SF_") else None)
    def test_navigate_to_search_from_sitemap(self, testcaseid, product, category, email, password):
        search_page = SearchPage(self.page)
        search_page.open_sitemap_search()
        page_title = search_page.page_heading()
        passed = page_title.strip().lower() == "search"
        self.assert_and_record(
            testcaseid, f"Sitemap navigation opened '{page_title}'.", passed
        )