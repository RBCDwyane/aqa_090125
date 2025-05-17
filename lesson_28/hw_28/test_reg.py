from .pages.homepage import HomePageLocators as Home
from .pages.garagepage import GaragePageLocators as Garage

def test_user_registration(driver, get_element, click_element, creds, delete_user):
    test_email = "testuser@qa.com"
    test_password = "Qwerty12"

    click_element(Home.signup_button)
    name_input = get_element(Home.signup_name)
    name_input.send_keys("Test")
    get_element(Home.signup_lastname).send_keys("User")
    get_element(Home.signup_email).send_keys(f"{test_email}")
    get_element(Home.signup_password).send_keys(f"{test_password}")
    get_element(Home.signup_password_reenter).send_keys("Qwerty12")
    click_element(Home.signup_register_button)
    profile_button = get_element(Garage.my_profile)

    assert profile_button.is_displayed()
    delete_user(test_email, test_password)