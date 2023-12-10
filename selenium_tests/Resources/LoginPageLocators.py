from selenium.webdriver.common.by import By


class LoginPageLocators():
    get_started_link = (By.XPATH, "/html/body/div/div/div[1]/header/button")
    login_button = "/html/body/div/div/div[1]/div[2]/div/a[1]"
    user_name = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/form/div[1]/input")
    password = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/form/div[2]/div/input")
    continue_button = "/html/body/div/div[3]/div/div/div[2]/div/form/button"
    user_name_error_message = "/html/body/div/div[3]/div/div/div[2]/div/form/div[1]/p"
    pw_error_message = "/html/body/div/div/div[2]/div[2]/div/form/p[2]"
    error_message_title = "/html/body/div/div[1]/ol/li/div/div[1]"
    error_message = "/html/body/div/div[1]/ol/li/div/div[2]"