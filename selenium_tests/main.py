import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.GetStartedPage import GetStartedPage
from Pages.LoginPage import LoginPage
from Pages.SIPCalculatorPage import SIPCalculatorPage


class TestRegistration(unittest.TestCase):
    """
    Run tests in headless mode.
    Base URL set to 127.0.0.1:3000 because of the github Actions page.
    Make sure to use XPATH where ever you can, because with CSS selectors the script running on github actions did not
    find the elements.
    """

    def setUp(self) -> None:
        options = Options()
        options.add_argument('--headless=new')

        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_url_and_title(self):
        """
        Testing whether the loaded page's url is the same as set in the base url.
        :return:
        """
        self.driver.get("http://127.0.0.1:3000/")
        self.assertEqual('http://127.0.0.1:3000/', self.driver.current_url)
        self.assertEqual('Finuncle', self.driver.title)

    def test_registration(self):
        """
        Test the 'Get Started' page on Finuncle. At the end of the process when all the fields are filled the button is
        disabled at the moment.
        """
        self.get_started_page = GetStartedPage(self.driver)
        alert_text = self.get_started_page.fill_out_registration_form_to_get_status_of_sign_up_button()

        self.assertEqual(alert_text, "Unexpected error occurred")


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.add_argument('--headless=new')

        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_login_with_unregistered_user(self):
        """
         Test login with an unregistered user.
         """
        self.login_page = LoginPage(self.driver)
        alert_text = self.login_page.fill_out_login_form_to_get_alert_text()
        self.assertEqual(alert_text, "Unexpected error occurred")

    def test_login_with_username_less_than_6_characters(self):
        self.login_page = LoginPage(self.driver)
        user_name_error_msg = self.login_page.fill_out_login_form_to_get_error_messages("asd")
        self.assertEqual(user_name_error_msg, "Enter at least 6 characters!")


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.add_argument('--headless=new')

        self.driver = webdriver.Chrome(options=options)

    def testSIPCalculationWithMinimalValues(self):
        self.sip_calculator_page = SIPCalculatorPage(self.driver)
        total_investment_value, final_value_text, wealth_gained_value = self.sip_calculator_page.set_values_to_calculator_parameters_to_get_summary(
            500, 1, 1)
        self.assertEqual(total_investment_value, "6000 ₹")
        self.assertEqual(final_value_text, "6028 ₹")
        self.assertEqual(wealth_gained_value, "28 ₹")


if __name__ == '__main__':
    unittest.main()
