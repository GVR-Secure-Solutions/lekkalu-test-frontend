import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage
from Resources.LoginPageLocators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://127.0.0.1:3000/signin')
        self.driver.set_window_size(1616, 876)

    def fill_out_login_form_to_get_alert_text(self):
        self.click(LoginPageLocators.user_name)
        self.enter_text(LoginPageLocators.user_name, "Qweasd")
        self.click(LoginPageLocators.password)
        self.enter_text(LoginPageLocators.password, "123456789")
        self.find_element_and_click(By.XPATH, LoginPageLocators.continue_button)
        time.sleep(3)
        alert_title = self.find_element(By.XPATH, LoginPageLocators.error_message_title).text
        return alert_title

    def fill_out_login_form_to_get_error_messages(self,username):
        self.click(LoginPageLocators.user_name)
        self.enter_text(LoginPageLocators.user_name, username)
        self.click(LoginPageLocators.password)
        self.find_element_and_click(By.XPATH, LoginPageLocators.continue_button)
        time.sleep(3)
        username_error_msg = self.find_element(By.XPATH, LoginPageLocators.user_name_error_message).text
        return username_error_msg



