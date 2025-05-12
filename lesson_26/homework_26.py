"""
Написати на python selenium код який пройде по двох фреймах на початковiй сторiнцi,
ввійде в кожний фрейм, введе правильний секретний текст, натисне кнопку “Перевiрити”,
порівняє текст дiалогового вiкна для підтвердження успішності верифікації та закриє діалогове вікно
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

url = f"http://localhost:8000/dz.html"
driver = webdriver.Chrome()
driver.get(url)

driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
input_field = driver.find_element(By.ID, "input1")
input_field.send_keys("Frame1_Secret")
check_button = driver.find_element(By.XPATH, '//button[@onclick="verifyInput(\'input1\')"]')
check_button.click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
input_field = driver.find_element(By.ID, "input2")
input_field.send_keys("Frame2_Secret")
check_button = driver.find_element(By.XPATH, '//button[@onclick="verifyInput(\'input2\')"]')
check_button.click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.quit()