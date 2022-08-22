from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

''' The Email and Password for test '''
email = "ahasanautomation@gmail.com"
password = "noitamotuanasaha"
app_password = "djbukoihlmamrixt"

url = 'https://localhost:4200/login/auth'


''' Bypassing "Google hasn't verified this app" '''
options = Options()
options.add_argument('--ignore-ssl-error=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(executable_path="C:\Web Drivers for Selenium\chromedriver_win32 (103)/chromedriver",
                          options=options)
driver.get(url)
driver.maximize_window()

# Login by google.
driver.find_element(By.XPATH, "//*[@id='gapi-signin2']/div[2]").click()

# Email Field.
driver.implicitly_wait(10)
driver.find_element(By.ID, "identifierId").send_keys(email)

driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span").click()

# Password field.
driver.implicitly_wait(10)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button/span").click()


''' Bypassing "Your Connection is not private blocker" '''
# Advanced
# driver.find_element(By.LINK_TEXT, "Advanced").click()
# driver.find_element(By.LINK_TEXT, "Go to ChatBookStaging (unsafe)").click()
# driver.find_element(By.XPATH, "//*[@id='submit_approve_access']/div/button/span").click()

''' Login By Facebook '''
# FACEBOOK LOGIN DOES NOT WORK FOR NOW
# # Login by facebook.
# driver.find_element(By.XPATH,"/html/body/app-root/div/app-login-index/div/div/div/app-group-auth/div/div/div/div[1]/div[2]").click()
#
# # Email Field
# driver.implicitly_wait(10)
# driver.find_element(By.ID, "email").send_keys(email)
#
# # Password Field
# driver.find_element(By.ID, "pass").send_keys(password)
#
# # login
# driver.find_element(By.ID, "loginbutton").click()

''' Registering the Organisation '''
# NO MORE COMES AFTER THE ORGANISATION HAS REGISTERED.
# driver.implicitly_wait(10)
# # Accepting cookies
# driver.find_element(By.XPATH, "/html/body/app-root/app-cookies-banner/div/div[2]/button[2]").click()
# driver.implicitly_wait(10)
# organisation_name = "Test Organisation"
# driver.find_element(By.XPATH, "//*[@id='group_form']/div[1]/input").send_keys(organisation_name)
#
# # agree to the terms and conditions
# driver.find_element(By.NAME, "termsCheckedField").click()
#
# # continue button
# driver.find_element(By.XPATH, "//*[@id='group_form']/button").click()

''' Building the first bot after new user registration '''
# driver.find_element(By.XPATH, "/html/body/app-root/div/app-layout/main/main/section/section/app-start-bot-creation/section/div/button").click()

''' Existing user creating a new bot  '''
## VERIFYING THAT CREATE BOT TAB IS OPEN HINT
# something = "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[1]/h5"
# if driver.find_element(By.XPATH, something):
#     print("Element exists")

''' Creating a New bot '''
# driver.implicitly_wait(10)
# bot_name = "Test bot_1"
# driver.find_element(By.NAME, "botName").clear()
# driver.find_element(By.NAME, "botName").send_keys(bot_name)
#
# # selecting from dropdown
# element = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[2]/div[2]/select")
# drp = Select(element)
#
# drp.select_by_visible_text("Facebook")
#
# # selecting language
# driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[2]/div[2]/div/button[2]").click()
#
# # Starting with  a template
# driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[3]/div[2]/div[3]/button").click()


driver.implicitly_wait(10)

# accepting the cookie
driver.find_element(By.XPATH, "/html/body/app-root/app-cookies-banner/div/div[2]/button[2]").click()

# selecting message option from the navigation bar
driver.find_element(By.XPATH, "/html/body/app-root/div/app-dashboard-main/div/main/app-sidebar/aside/nav/ul/li[2]/div/a[2]").click()

# creating a new topic
# driver.find_element(By.XPATH, "//*[@id='topicGroupScrollEl']/div[2]/div[1]/div[1]/span").click()

# creating another serie
plus_button = driver.find_element(By.XPATH, "//*[@id='cdk-drop-list-0']/div[2]/div[2]/div/app-serie-list/div/div[2]")
driver.execute_script("arguments[0].scrollIntoView();", plus_button)
# plus_button.click() -----> FOR CREATING ANOTHER SIRIE

driver.find_element(By.XPATH, "//*[@id='serie-249']/span").click()

# creating a text message
driver.find_element(By.XPATH, "//*[@id='tour-text-create']").click()

#writing a message
test_message = "Hello there its test message"
driver.find_element(By.XPATH, "//*[starts-with(@id, 'fbm-text-')]").send_keys(test_message)

#creating button
# driver.find_element(By.XPATH, "//*[starts-with(@id, 'msg-')]").click()     --------> not required

# popup - basically adding message from any other message

driver.find_element(By.XPATH, "//div[contains(@class, 'd-flex align-items-center width-fit popup-reply-add cursor-pointer default-msg-step-2 ug-tour-popup-create py-2 ng-star-inserted')]").click()

# creating a popup
driver.implicitly_wait(10)
popup_element = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-popup-modal/div/div[1]/div/select")
# popup_element.click()
drop = Select(popup_element)
drop.select_by_value("14: 1dcbb71d-4aea-42c9-b98c-77ffbdd97d01")

#adding the tag
tag_name = "Morning Tag"
driver.find_element(By.XPATH, "//*[@id='mat-chip-list-input-0']").send_keys(tag_name)

#closing the tag window for sirie

driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-popup-modal/div/form/div/a").click()

# Renaming everythinh
topic_rename = "Renamed Topic"
sirie_rename = "Rename Serie"
text_change = "Renamed Text"
popup_rename = "Rename Popup"
#Rename Topic
driver.find_element(By.XPATH, "/html/body/app-root/div/app-dashboard-main/div/main/div/app-build/div/div[2]/app-build-detail/div/div[1]/header/div[1]/input").clear()
driver.find_element(By.XPATH, "/html/body/app-root/div/app-dashboard-main/div/main/div/app-build/div/div[2]/app-build-detail/div/div[1]/header/div[1]/input").send_keys(topic_rename)
#Rename Serie
driver.find_element(By.XPATH, "/html/body/app-root/div/app-dashboard-main/div/main/div/app-build/div/div[2]/app-build-detail/div/div[1]/div/div/div/div[1]/div/input").clear()
driver.find_element(By.XPATH, "/html/body/app-root/div/app-dashboard-main/div/main/div/app-build/div/div[2]/app-build-detail/div/div[1]/div/div/div/div[1]/div/input").send_keys(sirie_rename)
#Text Change
driver.find_element(By.XPATH, "//*[starts-with(@id, 'fbm-text-')]").clear()
driver.find_element(By.XPATH, "//*[starts-with(@id, 'fbm-text-')]").send_keys(text_change)
#Popup rename
driver.find_element(By.XPATH, "//*[starts-with(@id, 'popupElement-')]").click()
driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-popup-modal/div/form/div/div/div[1]/input").clear()
driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-popup-modal/div/form/div/div/div[1]/input").send_keys(popup_rename)

#closing the popup window
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-popup-modal/div/form/div/a").click()