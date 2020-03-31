# This method is used to send the screenshot present in sspath to the contacts passed in the function parameter

from utils.send_img import send_img
from utils.seach import search_bar
from time import sleep
from random import randint

def send_ss(driver, sspath, tosend):
    for each in tosend:
        sleep(randint(2,5))                        # sleep is used to delay the scripts for 2-4 seconds
        search_bar(driver, each)
        send_img(driver, sspath)
