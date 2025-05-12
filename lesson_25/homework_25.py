"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"


driver = webdriver.Chrome()
driver.get(url)

xpath_element_1 = driver.find_element(By.XPATH, '//a[@class="header_logo"]')
xpath_element_2 = driver.find_element(By.XPATH, '//button[contains(@class, "header_signin")]')
xpath_element_3 = driver.find_element(By.XPATH, '//button[contains(@class, "-guest")]')
xpath_element_4 = driver.find_element(By.XPATH, '//a[contains(text(), "Home")]')
xpath_element_5 = driver.find_element(By.XPATH, '//button[@appscrollto="aboutSection"]')
xpath_element_6 = driver.find_element(By.XPATH, '//button[@appscrollto="contactsSection"]')
xpath_element_7 = driver.find_element(By.XPATH, '//h1[contains(@class, "hero-descriptor_title")]')
xpath_element_8 = driver.find_element(By.XPATH, '//p[contains(text(), "With the help of the Hillel auto project")]')
xpath_element_9 = driver.find_element(By.XPATH, '//div[@id="contactsSection"]')
xpath_element_10 = driver.find_element(By.XPATH, '//img[@src="/assets/images/homepage/info_2.jpg"]')
xpath_element_11 = driver.find_element(By.XPATH, '//img[@src="/assets/images/homepage/info_1.jpg"]')
xpath_element_12 = driver.find_element(By.XPATH, '//h2[text()="Contacts"]')
xpath_element_13 = driver.find_element(By.XPATH, '//p[text()="Log fuel expenses"]')
xpath_element_14 = driver.find_element(By.XPATH, '//a[@href="https://www.facebook.com/Hillel.IT.School"]')
xpath_element_15 = driver.find_element(By.XPATH, '//button[contains(text(), "Sign up")]')
xpath_element_16 = driver.find_element(By.XPATH, '//a[@href="https://t.me/ithillel_kyiv"]')
xpath_element_17 = driver.find_element(By.XPATH, '//div[@id="aboutSection"]')
xpath_element_18 = driver.find_element(By.XPATH, '//p[contains(text(), "repair your car yourself")]')
xpath_element_19 = driver.find_element(By.XPATH, '//a[@href="https://www.youtube.com/user/HillelITSchool?sub_confirmation=1"]')
xpath_element_20 = driver.find_element(By.XPATH, '//a[@href="https://www.instagram.com/hillel_itschool/"]')
xpath_element_21 = driver.find_element(By.XPATH, '//a[@href="https://www.linkedin.com/school/ithillel/"]')
xpath_element_22 = driver.find_element(By.XPATH, '//iframe[@class="hero-video_frame"]')

footer = driver.find_element(By.TAG_NAME, "footer")
driver.execute_script("arguments[0].scrollIntoView();", footer)
xpath_element_23 = driver.find_element(By.XPATH, '//a[text()="ithillel.ua"]')
xpath_element_24 = driver.find_element(By.XPATH, '//p[text()="Instructions and manuals"]')
xpath_element_25 = driver.find_element(By.XPATH, '//p[contains(text(), "replacement schedule")]')


css_element_1 = driver.find_element(By.CSS_SELECTOR, 'p.about-block_descr.lead')
css_element_2 = driver.find_element(By.CSS_SELECTOR, 'footer.footer')
css_element_3 = driver.find_element(By.CSS_SELECTOR, 'div.container')
css_element_4 = driver.find_element(By.CSS_SELECTOR, 'div.header_inner')
css_element_5 = driver.find_element(By.CSS_SELECTOR, 'div.header_right')
css_element_6 = driver.find_element(By.CSS_SELECTOR, 'div.app-wrapper')
css_element_7 = driver.find_element(By.CSS_SELECTOR, 'app-root')
css_element_8 = driver.find_element(By.CSS_SELECTOR, 'app-header')
css_element_9 = driver.find_element(By.CSS_SELECTOR, 'app-footer')
css_element_10 = driver.find_element(By.CSS_SELECTOR, 'app-home')
css_element_11 = driver.find_element(By.CSS_SELECTOR, 'div.guest-layout')
css_element_12 = driver.find_element(By.CSS_SELECTOR, 'section.hero')
css_element_13 = driver.find_element(By.CSS_SELECTOR, 'div.hero-descriptor')
css_element_14 = driver.find_element(By.CSS_SELECTOR, 'div.hero-video')
css_element_15 = driver.find_element(By.CSS_SELECTOR, 'div.about-block_picture')
css_element_16 = driver.find_element(By.CSS_SELECTOR, 'div.row')
css_element_17 = driver.find_element(By.CSS_SELECTOR, 'div.col-12.col-lg-6')
css_element_18 = driver.find_element(By.CSS_SELECTOR, 'div.contacts_socials')
css_element_19 = driver.find_element(By.CSS_SELECTOR, 'span.socials_icon.icon-facebook')
css_element_20 = driver.find_element(By.CSS_SELECTOR, 'span.socials_icon.icon-telegram')
css_element_21 = driver.find_element(By.CSS_SELECTOR, 'span.socials_icon.icon-youtube')
css_element_22 = driver.find_element(By.CSS_SELECTOR, 'span.socials_icon.icon-instagram')
css_element_23 = driver.find_element(By.CSS_SELECTOR, 'span.socials_icon.icon-linkedin')
css_element_24 = driver.find_element(By.CSS_SELECTOR, 'a.contacts_link.display-4')
css_element_25 = driver.find_element(By.CSS_SELECTOR, 'a.contacts_link.h4')


driver.quit()