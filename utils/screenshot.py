# This method is used to take the screenshot of the chat.

def take_screenshot(driver):
    driver.save_screenshot("screenshots/ss.png")
    print("Screenshot taken")
