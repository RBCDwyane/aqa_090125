"""
Створіть необхідні класи та функції, щоб за допомогою Selenium на сайті
https://tracking.novaposhta.ua/#/uk
ввести номер накладної (передається з тесту) та отримує статус посилки в теркінгу, наприклад:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NovaPoshtaTracking:
    def __init__(self, ttn_number):
        self.driver = webdriver.Chrome()
        self.url = "https://tracking.novaposhta.ua/#/uk"
        self.ttn_number = ttn_number
        self.status = self.track()

    def track(self):
        try:
            self.driver.get(self.url)

            input_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input#en'))
            )
            input_field.send_keys(self.ttn_number)

            search_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'np-number-input-desktop-btn-search-en'))
            )
            search_button.click()

            status_text = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
            ).text.strip()

            return status_text

        finally:
            self.driver.quit()

    def __str__(self):
        return self.status

if __name__ == "__main__":
    status = NovaPoshtaTracking("20451160306293")
    print(status)