from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


BRANCH_URL = "https://www.aihitdata.com/"

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BRANCH_URL


    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    

    def go_to_site(self):
        return self.driver.get(self.base_url)


    def scroll_to_element(self, locator):
        return self.driver.execute_script("return arguments[0].scrollIntoView(true);", self.find_element(locator))

    def find_invisibility(self, locator, time=50):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def find_presence_element(self, locator, time=5):
        # Если вернули True, то элемент есть
        # Если вернули False, то элемента на странице нет
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
            return True
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def find_clickable_element(self, locator, time=55):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))









