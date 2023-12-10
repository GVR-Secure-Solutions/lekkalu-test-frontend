import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Resources.SIPCalculatorPageLocators import SIPCalculatorPageLocators


class SIPCalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://127.0.0.1:3000/sip-calculator')
        self.driver.set_window_size(1616, 876)

    def set_values_to_calculator_parameters_to_get_summary(self, monthly_investment_amount, duration_of_investment,
                                                           expected_annual_return):
        self.clear_text(SIPCalculatorPageLocators.monthly_investment_amount)
        self.enter_text(SIPCalculatorPageLocators.monthly_investment_amount, monthly_investment_amount)
        self.clear_text(SIPCalculatorPageLocators.duration_of_investment)
        self.enter_text(SIPCalculatorPageLocators.duration_of_investment, duration_of_investment)
        self.clear_text(SIPCalculatorPageLocators.expected_annual_return)
        self.enter_text(SIPCalculatorPageLocators.expected_annual_return, expected_annual_return)
        total_value_text = self.find_element(By.XPATH, SIPCalculatorPageLocators.total_invested).text
        final_value_text = self.find_element(By.XPATH, SIPCalculatorPageLocators.final_value).text
        wealth_gained_text = self.find_element(By.XPATH, SIPCalculatorPageLocators.wealth_gained).text
        return total_value_text, final_value_text, wealth_gained_text
