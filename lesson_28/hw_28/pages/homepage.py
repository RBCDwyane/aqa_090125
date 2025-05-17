from selenium.webdriver.common.by import By

class HomePageLocators:
    signup_button = (By.XPATH,"//button[contains(@class, 'hero-descriptor_btn') and text() = 'Sign up']")
    signup_name = (By.XPATH,"//input[@id='signupName' and @name='name']")
    signup_lastname = (By.XPATH,"//input[@id='signupLastName' and @name='lastName']")
    signup_email = (By.XPATH,"//input[@id='signupEmail' and @name='email']")
    signup_password = (By.XPATH,"//input[@id='signupPassword' and @name='password']")
    signup_password_reenter = (By.XPATH,"//input[@id='signupRepeatPassword' and @name='repeatPassword']")
    signup_register_button = (By.XPATH,"//button[@type='button' and text()='Register']")