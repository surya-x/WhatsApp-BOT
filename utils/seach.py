# This method is used to type the parameter given to function into search bar of Whatsapp and will open the chat

from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

def search_bar(driver, parameter):
    print("Search bar called: ")
    search = driver.find_element_by_xpath('''//*[@id="side"]/div[1]/div/label/div/div[2]''')
    search.send_keys(parameter, Keys.RETURN)
    sleep(randint(2,5))                             # sleep is used to delay the scripts for 2-4 seconds
