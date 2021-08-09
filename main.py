from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

option = webdriver.ChromeOptions()
option.add_argument('window-size=1400,600')
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(executable_path='/Users/khangvu/Downloads/chromedriver', options=option)

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdLldhfK92S0TLezyFpR8-LupGCm7vbwPX4fHvmES5Wu0TQyw/viewform")
usernameStr = 'xxx@vntrip.vn'
passwordStr = '******'
username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))
time.sleep(5)
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "quantumWizTextinputPaperinputInput")))
time.sleep(5)
textboxes1 = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
textboxes1[0].send_keys("VNT_590")
textboxes1[1].send_keys("Vũ Mạnh Khang")
radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
now = datetime.now()
today17h = now.replace(hour=17, minute=0, second=0, microsecond=0)
if now < today17h:
    radiobuttons[0].click()
else:
    radiobuttons[1].click()
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "appsMaterialWizButtonPaperbuttonContent")))
submitbutton = browser.find_element_by_xpath("//*[contains(text(), 'Submit')]")
time.sleep(5)
submitbutton.click()
browser.close()
