from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import allure

class MainPageLocators:
    LOCATOR_FILTERS = (By.ID, "filtersHeading")
    LOCATOR_CHECKBOX_COMPANY_REGISTRATION = (By.ID, "hasRegnum")
    LOCATOR_CHECKBOX_WEBSITE = (By.ID, "hasWebsite")
    LOCATOR_CHECKBOX_EMAIL = (By.ID, "hasEmail")
    LOCATOR_CHECKBOX_PHONE = (By.ID, "hasPhone")
    LOCATOR_CHECKBOX_ADDRESS = (By.ID, "hasAddress")
    LOCATOR_BUTTON_SEARCH = (By.XPATH, "//button[text()='Search']")
    LOCATOR_COMPANY_NAME = (By.XPATH, "//*[@class='panel panel-default']/div[@class='panel-body']/div/a")


class MainPage(BasePage):
    def click_filters(self):
        return self.find_element(MainPageLocators.LOCATOR_FILTERS).click()

    def select_filters_checkbox(self):
        search_checkbox_company = self.find_clickable_element(MainPageLocators.LOCATOR_CHECKBOX_COMPANY_REGISTRATION)
        search_checkbox_company.click()
        search_checkbox_website = self.find_element(MainPageLocators.LOCATOR_CHECKBOX_WEBSITE)
        search_checkbox_website.click()
        search_checkbox_email = self.find_element(MainPageLocators.LOCATOR_CHECKBOX_EMAIL)
        search_checkbox_email.click()
        search_checkbox_phone = self.find_element(MainPageLocators.LOCATOR_CHECKBOX_PHONE)
        search_checkbox_phone.click()
        search_checkbox_address = self.find_element(MainPageLocators.LOCATOR_CHECKBOX_ADDRESS)
        search_checkbox_address.click()
        return search_checkbox_address

    def click_button_search(self):
        return self.find_element(MainPageLocators.LOCATOR_BUTTON_SEARCH).click()

    def search_company_name(self):
        all_list = self.find_elements(MainPageLocators.LOCATOR_COMPANY_NAME, time=2)
        company_name = [x.text for x in all_list if len(x.text) > 0]
        return company_name





