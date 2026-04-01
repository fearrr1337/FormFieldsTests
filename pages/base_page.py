import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def open(self, url):
        with allure.step(f'Open URL: {url}'):
            self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self,locator):
        with allure.step(f'Click element: {locator}'):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

    def send_keys(self,locator,text):
        with allure.step(f'Send keys {text} to element: {locator}'):
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)

    def get_alert_text(self):
        with allure.step("Get alert text"):
            alert = self.wait.until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            return text

    def take_screenshot(self, name="screenshot"):
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=name,
                      attachment_type=allure.attachment_type.PNG)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))