from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class FormPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    PASSWORD_INPUT = (By.ID, "password")
    DRINK_CHECKBOX = (By.CSS_SELECTOR, "input[name='drink'][value='{value}']")
    COLOR_RADIO = (By.XPATH, "//input[@name='color' and @value='{value}']")
    AUTOMATION_RADIO = (By.CSS_SELECTOR, "input[name='automation'][value='{value}']")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_TEXTAREA = (By.ID, "message")
    SUBMIT_BTN = (By.XPATH, "//button[text()='submit']")

    AUTOMATION_TOOLS_LABELS = (By.CSS_SELECTOR, "input[name='tools'] + label")
    AUTOMATION_TOOLS_LABELS_XPATH = (By.XPATH, "//input[@name='tools']/following-sibling::label")

    def __init__(self,driver):
        super().__init__(driver)
        self.url = "https://practice-automation.com/form-fields/"

    def open_page(self):
        self.open(self.url)
        return self

    def fill_name(self,name):
        self.send_keys(self.NAME_INPUT, name)
        return self

    def fill_password(self,psw):
        self.send_keys(self.PASSWORD_INPUT, psw)
        return self

    def select_drinks(self,*drinks):
        with allure.step(f"Selected drinks: {drinks}"):
            for drink in drinks:
                locator = (By.CSS_SELECTOR, self.DRINK_CHECKBOX[1].format(value=drink))
                self.click(locator)
        return self

    def select_color(self,color):
        locator = (By.XPATH, self.COLOR_RADIO[1].format(value=color))
        self.click(locator)
        return self

    def select_automation_option(self,option):
        locator = (By.CSS_SELECTOR, self.AUTOMATION_RADIO[1].format(value=option))
        self.click(locator)
        return self

    def fill_email(self,email):
        self.send_keys(self.EMAIL_INPUT, email)
        return self


    def fill_message_with_tools_info(self):
        tools_elements = self.find_elements(self.AUTOMATION_TOOLS_LABELS)
        if not tools_elements:
            tools_elements = self.find_elements(self.AUTOMATION_TOOLS_LABELS_XPATH)

        tools_names = [el.text.strip() for el in tools_elements if el.text.strip()]
        count = len(tools_names)
        if count > 0:
            longest_tool = max(tools_names, key=len)
        else:
            longest_tool = "None"

        message_text = f"Number of tools: {count}, Longest tool name: {longest_tool}"
        with allure.step(f"Fill message with: {message_text}"):
            self.send_keys(self.MESSAGE_TEXTAREA, message_text)
        return self


    def submit(self):
        self.click(self.SUBMIT_BTN)
        return self

    def get_alert_message(self):
        return self.get_alert_text()