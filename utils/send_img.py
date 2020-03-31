# This method is used to send the image to a chat which is already opened.

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from random import randint

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
