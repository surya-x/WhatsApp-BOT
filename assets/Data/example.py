from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument(r"user-data-dir=C:\Users\chief_surya01\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com")
