from selenium.webdriver.common.by import By


class SIPCalculatorPageLocators():
    monthly_investment_amount = (By.XPATH, "/html/body/div/div[3]/div/div[3]/div[1]/div[1]/form/div[1]/div/div/input")
    duration_of_investment = (By.XPATH, "/html/body/div/div[3]/div/div[3]/div[1]/div[1]/form/div[2]/div/div/input")
    expected_annual_return = (By.XPATH, "/html/body/div/div[3]/div/div[3]/div[1]/div[1]/form/div[3]/div/div/input")
    total_invested = "/html/body/div/div[3]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]"
    final_value = "/html/body/div/div[3]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[2]"
    wealth_gained = "/html/body/div/div[3]/div/div[3]/div[1]/div[2]/div[2]/div[3]/div[2]"