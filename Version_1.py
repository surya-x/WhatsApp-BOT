'''
The Version 1 will do the following tasks:
> It will work For each contact in "contact.xlsx"
> It will check for any unread messages for the contact in "contacts.xlsx" under column B
> If there are unread messages it will take the screenshot of the chat
> It will send the respective message for a contact from "contact.xlsx" under column D
> It will then send the gift.png to the contact
> It will send the screenshot to all contacts listed in "parameter.xlsx" under column A
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from utils import check_unread_msgs, send_img, send_ss, search_bar, take_screenshot, send_msg
from utils import establishing_conn_withExcel
from config import contacts_filePath, parameters_filePath, imagepath, sspath

import xlrd
from time import sleep
from random import randint


options = Options()

options.add_argument(r"user-data-dir=C:\Users\chief_surya01\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)

print("Please scan the QR code to login into Whatsapp")
driver.get("https://web.whatsapp.com")

try:                                                            # To wait until the page loads
    element = WebDriverWait(driver, 600).until(
        EC.presence_of_element_located((By.XPATH, ''' //*[@id="pane-side"]/div[1]/div/div/div '''))
    )
except TimeoutException as Exception:
     print("Failed logging Whatsapp \nStart again...")
     driver.quit()
else:
    print("QR code scanned, You are logged into Whatsapp")


excel_data = {}
excel_data['namelist']    = []
excel_data['msglist']     = []
excel_data['numlist']     = []
excel_data['forwardlist'] = []



# for establishing connection with excel

print("===================Excel contents================================== ")

excel_data = establishing_conn_withExcel(contacts_filePath, parameters_filePath)
# print(excel_data['namelist'], excel_data['msglist'], excel_data['numlist'], excel_data['forwardlist'])

print("=====================Excel contents printed======================== ")

# To iterate each name in contacts.xlsx and execute code

for name, msg, num in zip(excel_data['namelist'], excel_data['msglist'], excel_data['numlist']):
    print("For contact :", name)
    unread_msgs_count = check_unread_msgs(driver, name)  # change method name to check_unread_msgs()

    print("Unread_msgs: ", unread_msgs_count)
    unread_msgs_count = int(unread_msgs_count)

    search_bar(driver, name)                             # name should be saved in phone contacts

    if unread_msgs_count > 0:
        take_screenshot(driver)

    send_msg(driver, msg)

    send_img(driver, imagepath)

    if unread_msgs_count > 0:
        send_ss(driver, sspath, excel_data['forwardlist'])

    print("Sending message to %s success"%name)
    sleep(randint(4,7))
