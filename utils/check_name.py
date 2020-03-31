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
