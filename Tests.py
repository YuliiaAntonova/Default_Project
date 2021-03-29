from MainPages import MainPage
import time
import random
import allure


@allure.severity(allure.severity_level.CRITICAL)
def test_filter_checkbox(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.click_filters()
    main_page.select_filters_checkbox()
    main_page.click_button_search()
    time.sleep(5)

    # TODO добавь про проверку
    result = main_page.search_company_name()
    print()
    print(f"Company name list: {result}")
