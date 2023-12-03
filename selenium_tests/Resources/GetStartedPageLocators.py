from selenium.webdriver.common.by import By


class GetStartedPageLocators():
    get_started_link = (By.XPATH, "/html/body/div/div/div[1]/header/button")
    user_name = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/form/div[1]/input")
    email = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/form/div[2]/input")
    password = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/form/div[3]/div/input")
    terms_and_conditions = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/form/div[4]/div/button")
    privacy_policy = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/form/div[5]/div/button")
    signup_button = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/form/button")
    error_message_title = "/html/body/div/div[1]/ol/li"

