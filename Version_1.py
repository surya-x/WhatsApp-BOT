'''
The Version 1 will do the following tasks:
> It will work For each contact in "contact.xlsx"
> It will check for any unread messages for the contact in "contacts.xlsx" under column B
> If there are unread messages it will take the screenshot of the chat
> It will send the respective message for a contact from "contact.xlsx" under column D
> It will then send the gift.png to the contact
> It will send the screenshot to all contacts listed in "parameter.xlsx" under column A
'''

from utils import check_unread_msgs, send_img, send_ss, search_bar, take_screenshot, send_msg
from utils import establishing_conn_withExcel, connecting_with_whatsapp
from config import contacts_filePath, parameters_filePath, imagepath, sspath
from time import sleep
from random import randint




excel_data = {}
excel_data['namelist']    = []
excel_data['msglist']     = []
excel_data['numlist']     = []
excel_data['forwardlist'] = []


driver = connecting_with_whatsapp()

# for establishing connection with excel
print("===================Excel contents================================== ")

excel_data = establishing_conn_withExcel(contacts_filePath, parameters_filePath)
print(excel_data['namelist'], excel_data['msglist'], excel_data['numlist'], excel_data['forwardlist'])

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
