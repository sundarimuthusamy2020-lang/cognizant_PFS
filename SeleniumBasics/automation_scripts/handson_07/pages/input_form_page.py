from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InputFormPage(BasePage):

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "inputEmail4")
    PHONE = (By.ID, "inputPassword4")
    ADDRESS = (By.ID, "company")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS = (By.CLASS_NAME, "success-msg")

    def fill_form(self, name, email, phone, address):

        self.wait_for_element(self.NAME).send_keys(name)
        self.wait_for_element(self.EMAIL).send_keys(email)
        self.wait_for_element(self.PHONE).send_keys(phone)
        self.wait_for_element(self.ADDRESS).send_keys(address)

    def submit_form(self):
        self.wait_for_element(self.SUBMIT).click()

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS).text