# This method is used to type and send the msg the chat which is already opened.

from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

def send_msg(driver, msg):
    print("sending message: ", msg)
    sleep(randint(2,5))                        # sleep is used to delay the scripts for 2-4 seconds
    typ = driver.find_element_by_xpath('''//*[@id="main"]/footer/div[1]/div[2]''')
    typ.send_keys(msg, Keys.RETURN)
