from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error'")


def open_page(self):
    self.driver.get("https://www.saucedemo.com")
    return self

def login_as_valid_user(self, username, password):
    self._fill_login_form(username, password)

    return InventoryPage(self.driver)
def login_error(self, username, password):
    self._fill_login_form(username, password)
    return self

def get_error_text(self):
    return self.driver.find_element(*self.ERROR_MESSAGE).text
