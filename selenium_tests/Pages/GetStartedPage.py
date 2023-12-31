import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Resources.GetStartedPageLocators import GetStartedPageLocators


class GetStartedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://127.0.0.1:3000/signup')
        self.driver.set_window_size(1616, 876)

    def fill_out_registration_form_to_get_status_of_sign_up_button(self):
        # self.click(GetStartedPageLocators.get_started_link)
        self.click(GetStartedPageLocators.user_name)
        self.enter_text(GetStartedPageLocators.user_name, "Qweasd")
        self.click(GetStartedPageLocators.email)
        self.enter_text(GetStartedPageLocators.email, "asd@asd.com")
        self.click(GetStartedPageLocators.password)
        self.enter_text(GetStartedPageLocators.password, "123456789")
        self.click(GetStartedPageLocators.terms_and_conditions)
        self.click(GetStartedPageLocators.privacy_policy)
        self.click(GetStartedPageLocators.signup_button)
        time.sleep(3)
        alert_title = self.find_element(By.XPATH, GetStartedPageLocators.error_message_title).text
        return alert_title
