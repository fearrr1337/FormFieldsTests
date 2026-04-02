import pytest
from selenium import webdriver
import allure


@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    def fin():
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot_on_failure",
                          attachment_type=allure.attachment_type.PNG)
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)