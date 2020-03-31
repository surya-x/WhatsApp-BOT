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

from utils.check_name import check_unread_msgs
from utils.send_img import send_img
from utils.send_ss import send_ss
from utils.seach import search_bar
from utils.screenshot import take_screenshot
from utils.send_message import send_msg

from config import contacts_filePath
from config import parameters_filePath
from config import imagepath
from config import sspath

import xlrd
from time import sleep
from random import randint

def establishing_conn_withExcel(contacts_filePath, parameters_filePath):
    wb1 = xlrd.open_workbook(contacts_filePath)
    wb2 = xlrd.open_workbook(parameters_filePath)

    sheet1 = wb1.sheet_by_index(0)
    sheet2 = wb2.sheet_by_index(0)

    for i in range(1, sheet1.nrows):
        namelist.append(sheet1.cell_value(i, 1))
        msglist.append(sheet1.cell_value(i, 3))
        numlist.append(sheet1.cell_value(i, 2))

    for i in range(1, sheet2.nrows):
        forwardlist.append(sheet2.cell_value(i, 0))

options = Options()

options.add_argument(r"user-data-dir=C:\Users\chief_surya01\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com")

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


namelist    = []
msglist     = []
numlist     = []
forwardlist = []

# for establishing connection with excel

print("===================Excel contents================================== ")

establishing_conn_withExcel(contacts_filePath, parameters_filePath)
print(namelist, msglist, numlist, forwardlist)

print("=====================Excel contents printed======================== ")

# To iterate each name in contacts.xlsx and execute code

for name, msg, num in zip(namelist, msglist, numlist):
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
        send_ss(driver, sspath, forwardlist)

    print("Sending message to %s success"%name)
    sleep(randint(4,7))
