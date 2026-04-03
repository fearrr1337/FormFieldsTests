from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure

class FormPage(BasePage):
    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    DRINK_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='{value}']")
    COLOR_RADIO = (By.CSS_SELECTOR, "input[type='radio'][value='{value}']")
    AUTOMATION_SELECTOR = (By.ID, "automation")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_TEXTAREA = (By.ID, "message")
    AUTOMATION_TOOLS_LABELS = (By.XPATH, "//label[text()='Automation tools']/following-sibling::ul/li")
    AUTOMATION_TOOLS_LABELS_XPATH = (By.XPATH, "//label[text()='Automation tools']/following-sibling::ul/li")
    SUBMIT_BTN = (By.ID, "submit-btn")



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
        with allure.step(f"Selected color: {color}"):
            locator = (By.CSS_SELECTOR, self.COLOR_RADIO[1].format(value=color))
            self.click(locator)
        return self

    def select_automation_option(self,option):
        with allure.step(f"Select automation option: {option}"):
            select_element = self.wait.until(EC.presence_of_element_located(self.AUTOMATION_SELECTOR))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", select_element)
            select = Select(select_element)
            select.select_by_visible_text(option)
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
        longest_tool = max(tools_names, key=len) if count > 0 else "None"

        message_text = f"Number of tools: {count}, Longest tool name: {longest_tool}"
        with allure.step(f"Fill message with: {message_text}"):
            self.send_keys(self.MESSAGE_TEXTAREA, message_text)
        return self


    def submit(self):
        self.click(self.SUBMIT_BTN)
        return self

    def get_alert_message(self):
        return self.get_alert_text()