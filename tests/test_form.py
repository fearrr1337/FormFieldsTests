import allure
import pytest
from pages.form_page import FormPage


@allure.feature("Form Fields")
@allure.story("Submit form and verify alert")
def test_submit_form(driver):
    with allure.step("Open form page"):
        form_page = FormPage(driver)
        form_page.open_page()

    with allure.step("Fill form fields"):
        form_page.fill_name("Test User") \
                .fill_password("Secret123") \
                .select_drinks("Milk", "Coffee") \
                .select_color("Yellow") \
                .select_automation_option("Yes") \
                .fill_email("user@example.com") \
                .fill_message_with_tools_info() \
                .submit()

    with allure.step("Verify alert message"):
        alert_text = form_page.get_alert_message()
        assert alert_text == "Message received!", f"Expected 'Message received!', got '{alert_text}'"

    form_page.take_screenshot("success_screenshot")