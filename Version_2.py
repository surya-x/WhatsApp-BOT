'''
The Version 2 will do the following tasks:
> It will work For each contact in "contact.xlsx"
> It will send the respective message for a contact from "contact.xlsx" under column D
> It will then send the gift.png to the contact
'''

from app.utils import send_img, search_bar, send_msg
from app.utils import establishing_conn_withExcel, connecting_with_whatsapp
from config import contacts_filePath, parameters_filePath, imagepath, logging
from time import sleep
from random import randint

excel_data = {}
excel_data['namelist'] = []
excel_data['msglist'] = []
excel_data['numlist'] = []
excel_data['forwardlist'] = []


driver = connecting_with_whatsapp()

try:

	# for establishing connection with excel
	excel_data = establishing_conn_withExcel(
	    contacts_filePath, parameters_filePath)

	# To iterate each name in contacts.xlsx and execute code
	for name, msg, num in zip(excel_data['namelist'], excel_data['msglist'], excel_data['numlist']):
		logging.info("======For contact :" + name + " | msg: " + msg)

		search_bar(driver, name)                             # name should be saved in phone contacts
		send_msg(driver, msg, name)
		send_img(driver, imagepath)

		logging.info("=======Sending message to %s success"%name)
		sleep(randint(4,7))

except Exception as e:
    print("Error Occured!!")
    logging.error(e)
finally:
    # print("Task Completed!")
    driver.quit()
