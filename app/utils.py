from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
import xlrd
import logging


def connecting_with_whatsapp():
    logging.info("Connecting with whatsapp")
    options = Options()

    # options.add_argument(
    #     r"user-data-dir=C:\Users\chief_surya01\AppData\Local\Google\Chrome\User Data")
    
    driver = webdriver.Chrome(options=options)

    # print("Please scan the QR code if prompted to login into Whatsapp")
    driver.get("https://web.whatsapp.com")

    try:                                                            # To wait until the page loads
        element = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located(
                (By.XPATH, ''' //*[@id="pane-side"]/div[1]/div/div/div '''))
        )
    except TimeoutException as Exception:
        logging.error("Failed logging Whatsapp \nStart again...")
    except NoSuchElementException as Exception:
        logging.error("NoSuchElementException found..")
    except Exception as e:
        logging.error("Exception found in connecting_with_whatsapp")
        logging.error(e)
    else:
        logging.info("QR code scanned, You are logged into Whatsapp")

    return driver


def establishing_conn_withExcel(contacts_filePath, parameters_filePath):
    logging.info("EStablishing connection with excel")
    data = {}
    data['namelist'] = []
    data['msglist'] = []
    data['numlist'] = []
    data['forwardlist'] = []

    try:

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

    except Exception as e:
        logging.error("Exception found in establishing_conn_withExcel")
        logging.error(e)
    return data


# This method is used to send the screenshot present in sspath to the
# contacts passed in the function parameter
def send_ss(driver, sspath, tosend):
    logging.info("Sending screenshot to contacts: ")
    try:

        for each in tosend:
            # sleep is used to delay the scripts for 2-4 seconds
            sleep(randint(2, 5))
            search_bar(driver, each)
            send_img(driver, sspath)

    except Exception as e:
        logging.error("Exception found in send_ss")
        logging.error(e)


# This method is used to type and send the msg the chat which is already
# opened.
def send_msg(driver, msg, name):
    logging.info("sending message: " + msg)
    try:
        # sleep is used to delay the scripts for 2-4 seconds
        sleep(randint(2, 5))
        typ = driver.find_element_by_xpath(
            '''//*[@id="main"]/footer/div[1]/div[2]''')
        typ.send_keys(msg, Keys.RETURN)
    except NoSuchElementException as Exception:
        logging.error("NoSuchElementException found in send_msg")
        logging.error(e)
        print("Name not found for sending msg: " + name)
    except Exception as e:
        logging.error("Exception found in send_msg")
        logging.error(e)



# This method is used to send the image to a chat which is already opened.
def send_img(driver, imgpath):
    logging.info("Sending image to open chats: ")
    try:

        # sleep is used to delay the scripts for 1-3 seconds
        sleep(randint(1, 4))
        driver.find_element_by_css_selector("span[data-icon = 'clip']").click()

        # sleep is used to delay the scripts for 1-3 seconds
        sleep(randint(1, 4))
        driver.find_element_by_css_selector(
            "input[type='file']").send_keys(imgpath)

        send = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span[data-icon='send-light']"))
        )
        # sleep is used to delay the scripts for 1-2 seconds
        sleep(randint(1, 3))
        send.click()
    except NoSuchElementException as Exception:
        logging.error("NoSuchElementException found in send_img")
        logging.error(e)
    except Exception as e:
        logging.error("Exception found in send_img")
        logging.error(e)


# This method is used to type the parameter given to function into search
# bar of Whatsapp and will open the chat
def search_bar(driver, parameter):
    logging.info("search_bar called: ")
    try:
        search = driver.find_element_by_xpath(
            '''//*[@id="side"]/div[1]/div/label/div/div[2]''')
        search.clear()
        search.send_keys(parameter, Keys.RETURN)
        # sleep is used to delay the scripts for 2-4 seconds
        sleep(randint(2, 5))

    except NoSuchElementException as Exception:
        logging.error("NoSuchElementException found in search_bar")
        logging.error(e)
    except Exception as e:
        logging.error("Exception found in search_bar")
        logging.error(e)


# This method is used to check for unread messages if there are any
def check_unread_msgs(driver, name):
    logging.info("check unread msgs called: ")
    try:

        allcontacts = driver.find_elements_by_xpath(
            ''' //*[@id="pane-side"]/div[1]/div/div/div ''')

        # return -1 if the name is not there
        unread_msgs_count = -1
        for contact in allcontacts:
            stringlist = contact.text.split("\n")
            name1 = stringlist[0]
            if name1.lower() == name.lower():
                if len(stringlist) > 3:
                    # return no of unread msg if its there
                    unread_msgs_count = stringlist[3]
                else:
                    unread_msgs_count = 0               # return 0 if there's no unread msg there

        if unread_msgs_count == ":":                    # NOTE: Mute chats are treated as 0 unread messages
            unread_msgs_count = 0

        logging.info("unread_msgs_count: " + str(unread_msgs_count))
        return unread_msgs_count

    except Exception as e:
        logging.error("Exception found in check_unread_msgs")
        logging.error(e)

# This method is used to take the screenshot of the chat.
def take_screenshot(driver, sspath):
    logging.info("taking screenshot is called: ")
    try:
        driver.save_screenshot(sspath)
        logging.info("Screenshot taken")

    except Exception as e:
        logging.error("Exception found in take_screenshot")
        logging.error(e)
