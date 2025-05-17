import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

@pytest.fixture(scope="session")
def creds():
    return {
        "user": "guest",
        "password": "welcome2qauto"
    }

@pytest.fixture(scope="session")
def driver(creds):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://{creds['user']}:{creds['password']}@qauto2.forstudy.space/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def get_element(driver):
    def _get(locator, timeout=3):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    return _get

@pytest.fixture
def click_element(get_element):
    def _click(locator):
        element = get_element(locator)
        element.click()
    return _click

@pytest.fixture
def delete_user():
    def _delete(email, password):
        session = requests.Session()
        login_resp = session.post(f"https://qauto2.forstudy.space/api//auth/signin", json={
            "email": email,
            "password": password
        })
        login_resp.raise_for_status()
        response = session.delete("https://qauto2.forstudy.space/api/users")
        response.raise_for_status()
    return _delete