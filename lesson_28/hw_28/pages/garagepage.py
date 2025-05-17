from selenium.webdriver.common.by import By

class GaragePageLocators:
    header = (By.XPATH,'//h1[contains(text(), "Garage")]')
    my_profile = (By.ID, "userNavDropdown")