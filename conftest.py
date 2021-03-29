import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


# путь к драйверу
EXEC_PATH = 'drivers/chromedriver'
WINDOW_SIZE_WIDTH = 1920
WINDOW_SIZE_HEIGHT = 1080

# используется в remote browser
capabilities = {
    "browserName": "chrome",
    "version": "84.0",
    "enableVNC": True,
    "enableVideo": False
}

@pytest.fixture(scope="session")
def browser():
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=EXEC_PATH, chrome_options=options)
    # driver = webdriver.Remote(command_executor="http://10.69.69.215:4444/wd/hub", desired_capabilities=capabilities)
    driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))



