from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re
import sys
import random

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_extension('/home/endu/Downloads/AdBlock — best ad blocker(4.46.0)2022-04-24.crx')
driver = webdriver.Chrome(options=options, executable_path=r"chromedriver")

# to skirt adblock first-run notification

while len(driver.window_handles) == 1:
        sleep(1)

killed=False

while not killed:
        for i in driver.window_handles:
                driver.switch_to.window(i)
                if driver.title == 'AdBlock is now installed!':
                        driver.close()
                        killed=True

driver.switch_to.window(driver.window_handles[0])

tempmail_url='https://tempail.com'
password='Moron101!@p3rth4ustral1a'
email_address=''
huawei_registeration_page_url='https://uniportal.huawei.com/accounts/register.do?method=toRegister&regsiterMethod=byEmail&nls=en_US&appurl=https%3A%2F%2Funiportal.huawei.com%2Fsaaslogin%2Fidp%3FRelayState%3Duniportal_talent%26SAMLRequest%3DfVPbjtowEH3fr0B5Dw4JuywWSUWhFyQWIkirqi8r4wyLpcRO7Qlh%2F77OZVlatfFDEo3POXPmkplheVbQeYknuYNfJRi8G9hzyTNpaHMZOqWWVDEjDJUsB0OR0%2F38aU39oUcLrVBxlTl%2F0fpZzBjQKJRsaatl6Gw3n9bbL6vN8yR4YGkw8R4fJ0Ew9XnqT%2FwpHPgYgkNwnI4P6T33xsFDS%2F0O2lid0LGybSTW6ixS0BubNXSqqnoWa2BaCvnyo0tnTAkraZBJtETP913v3vWDZBTQ0ZQG458tbmm7ISTDRv%2BEWBhKSClFoTSybHgqWQViyFVODGMmUy9CEpEWH4rOQWhRILEDWuK5NouvNeXqteneRyFT66%2B%2FaYcWZOjXJIndeLtPWpH5WzMXSpoyB70HfRYcvu3W77Z7rBBmp0%2FsR5EBAsGCufUESaseNc9ZHaFN43TUozUjt8B3akHrcayWscoEf23i9fmsdM7w%2F2WPhqMmIlL32EBpKU0BXBwFpM5VZp5lqlpoYGgnjroEZ0D%2BSN6tNqTNots%2BIVxwsLAlMy1MPV64MI5OdJVsC76FLzK7tTs4Rr2LzSmvcTYc21eldFrPGLjNnWhmzdvd6Zr0T%2FHWNemxHd29Xd%2F%2BtdFv%26provider%3Dtalent.huaweiuniversity.com%26pname%3Dtalent.huaweiuniversity.com-pend'

try:
	driver.get(tempmail_url)
except Exception as e:
	print('failed to get '+tempmail_url)
	driver.close()
	driver.quit()
	exit(1)

while not email_address:
        try:
                if driver.find_element(by=By.ID, value='eposta_adres'):
                        email_address = driver.find_element(by=By.ID, value='eposta_adres').get_property('value')
                        if not re.search('^\w+@\w+\.\w+$', email_address):
                                email_address=''
                if not email_address:
                        sleep(2)
        except Exception as e:
                pass

username=re.subn('@[\w\d]+\.[\w\d]+$','',email_address)[0]+str(random.randint(10000,20000))

try:
	driver.get(huawei_registeration_page_url)
except Exception as e:
	print('failed to get '+tempmail_url)
	driver.close()
	driver.quit()
	exit(1)

driver.find_element(by=By.ID, value='registerVO.userId').send_keys(username)
driver.find_element(by=By.ID, value='registerVO.email').send_keys(email_address)
driver.find_element(by=By.ID, value='registerVO.password').send_keys(password)
driver.find_element(by=By.ID, value='registerVO.givenname').send_keys('Aerton')
driver.find_element(by=By.ID, value='registerVO.surname').send_keys('Senna')
e=driver.find_element(by=By.ID, value='countryCodeSelect')
for i in range(1, random.randint(4,20)):
	e.send_keys(webdriver.common.keys.Keys.DOWN)
# driver.find_element(by=By.ID, value='registerVO.verifycode').send_keys(input('whats the captcha? '))

driver.find_element(by=By.ID, value='agreement').click()
driver.find_element(by=By.ID, value='regbtn').click()

# email verification

try:
	driver.get(tempmail_url)
except Exception as e:
	print('failed to get '+tempmail_url)
	driver.close()
	driver.quit()
	exit(1)

# wait till email gets here
while driver.page_source.find("Please activate your Huawei website account") == -1:
        sleep(5)
        try:
                driver.find_element(by=By.CLASS_NAME, value='yenile-link').click() # refresh button press
        except Exception as e:
                pass

try:
        driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Please activate your Huawei website account").click()
except Exception as e:
        pass

try:
        driver.switch_to.frame(driver.find_element(by=By.TAG_NAME, value='iframe'))
except Exception as e:
        pass

verification_link=""

while not verification_link:
        for a in driver.find_elements(by=By.TAG_NAME, value='a'):
                if re.search('^https:\/\/uniportal\.huawei\.com\/accounts\/register\.do.+$', a.get_attribute('href')):
                        verification_link=a.get_attribute('href')

driver.get(verification_link)

################ EVERYTHING AFTER THIS IS SHIT

# driver.find_element(by=By.CLASS_NAME, value='lang-en').click()

# # hit the login button

# while driver.page_source.find('Get your third-party account username, email, mobile number and name registration information.') == -1:
# 	sleep(5)

# driver.find_element(by=By.ID, value='registerModalConfirm').click()
# driver.find_element(by=By.CSS_SELECTOR, value='span.el-checkbox__input').click()
# driver.find_element(by=By.CSS_SELECTOR, value='#app > div.el-dialog__wrapper.protocol-modal > div > div.el-dialog__footer > span > button.el-button.el-button--primary').click()
# # going to the HCIA AI v3.0 page
# driver.get('https://talent.huaweiuniversity.com/portal/courses/HuaweiX+EBG2020CCHW1100087/about')
# while driver.page_source.find('Enroll Now') == -1:
# 	sleep(3)

# driver.find_element(by=By.CSS_SELECTOR, value='#main > div > div > section > div.course-about-header > div.courses-header-right.mooc > div.class-button > div:nth-child(2) > button').click()
# sleep(2)
# driver.find_element(by=By.CSS_SELECTOR, value='input.el-input__inner').send_keys('Aerton Senna')
# driver.find_element(by=By.CSS_SELECTOR, value='#main > div > div > section > div.course-about-header > div.courses-header-right.mooc > div.class-button > div.el-dialog__wrapper.confirm-username-modal > div > div.el-dialog__body > form > div.el-form-item.action.text-right.el-form-item--feedback.el-form-item--medium > div > div > button').click()
# # getting the mock exam
# driver.get('https://talent.huaweiuniversity.com/portal/exam/104133/about?lang=en_US')
# while driver.page_source.find('Start exam') == -1:
# 	sleep(3)