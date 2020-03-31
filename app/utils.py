from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
import xlrd



def connecting_with_whatsapp():
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

	return driver



def establishing_conn_withExcel(contacts_filePath, parameters_filePath):
    data = {}
    data['namelist'] = []
    data['msglist'] = []
    data['numlist'] = []
    data['forwardlist'] = []

    wb1 = xlrd.open_workbook(contacts_filePath)
    wb2 = xlrd.open_workbook(parameters_filePath)

    sheet1 = wb1.sheet_by_index(0)
    sheet2 = wb2.sheet_by_index(0)

    for i in range(1, sheet1.nrows):
        data['namelist'].append(sheet1.cell_value(i, 1))
        data['msglist'].append(sheet1.cell_value(i, 3))
        data['numlist'].append(sheet1.cell_value(i, 2))

    for i in range(1, sheet2.nrows):
        data['forwardlist'].append(sheet2.cell_value(i, 0))

    return data



# This method is used to send the screenshot present in sspath to the contacts passed in the function parameter
def send_ss(driver, sspath, tosend):
    for each in tosend:
        sleep(randint(2,5))                        # sleep is used to delay the scripts for 2-4 seconds
        search_bar(driver, each)
        send_img(driver, sspath)


# This method is used to type and send the msg the chat which is already opened.
def send_msg(driver, msg):
    print("sending message: ", msg)
    sleep(randint(2,5))                        # sleep is used to delay the scripts for 2-4 seconds
    typ = driver.find_element_by_xpath('''//*[@id="main"]/footer/div[1]/div[2]''')
    typ.send_keys(msg, Keys.RETURN)


# This method is used to send the image to a chat which is already opened.
def send_img(driver, imgpath):
    sleep(randint(1, 4))                        # sleep is used to delay the scripts for 1-3 seconds
    driver.find_element_by_css_selector("span[data-icon = 'clip']").click()

    sleep(randint(1, 4))                        # sleep is used to delay the scripts for 1-3 seconds
    driver.find_element_by_css_selector("input[type='file']").send_keys(imgpath)

    send = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='send-light']"))
    )
    sleep(randint(1, 3))                        # sleep is used to delay the scripts for 1-2 seconds
    send.click()



# This method is used to type the parameter given to function into search bar of Whatsapp and will open the chat
def search_bar(driver, parameter):
    print("Search bar called: ")
    search = driver.find_element_by_xpath('''//*[@id="side"]/div[1]/div/label/div/div[2]''')
    search.send_keys(parameter, Keys.RETURN)
    sleep(randint(2,5))                             # sleep is used to delay the scripts for 2-4 seconds


# This method is used to check for unread messages if there are any
def check_unread_msgs(driver, name):
    print("check unread msgs called: ")
    allcontacts = driver.find_elements_by_xpath(''' //*[@id="pane-side"]/div[1]/div/div/div ''')

    unread_msgs_count = -1                          # return -1 if the name is not there
    for contact in allcontacts:
        stringlist = contact.text.split("\n")
        name1 = stringlist[0]
        if name1.lower() == name.lower():
            if len(stringlist) > 3:
                unread_msgs_count = stringlist[3]   # return no of unread msg if its there
            else:
                unread_msgs_count = 0               # return 0 if there's no unread msg there

    if unread_msgs_count == ":":                    # NOTE: Mute chats are treated as 0 unread messages
        unread_msgs_count = 0

    return unread_msgs_count


# This method is used to take the screenshot of the chat.
def take_screenshot(driver):
    driver.save_screenshot("screenshots/ss.png")
    print("Screenshot taken")
