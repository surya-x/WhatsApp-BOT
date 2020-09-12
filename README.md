# What'sApp Automation For Business
 
This can be used to Partially Automate your whatsapp messages, features including checking for 
unread messages, forwarding unread messages of all/selected contacts to your social media handler/
secretary. 
It will also help you to forward any text/image to any number of contacts.
 
This project is build with 4 versions, which work as :- 

## The Version 1 will do the following tasks:
  It will check for any unread messages for all the chat (excluding groups)
  Note :- It will treat mute chats as no unread messages
  If there are unread messages it will take the screenshot of the chat
  It will send the screenshot to all contacts listed in "parameter.xlsx" under column A
  It will work For each contact in "contact.xlsx"
  It will send the respective message for a contact from "contact.xlsx" under column D
  It will then send the gift.png to the contact

## The Version 2 will do the following tasks:
  It will work For each contact in "contact.xlsx"
  It will send the respective message for a contact from "contact.xlsx" under column D
  It will then send the gift.png to the contact

## The Version 3 will do the following tasks:
  It will check for any unread messages for all the chat (excluding groups)
  Note :- It will treat mute chats as no unread messages
  If there are unread messages it will take the screenshot of the chat
  It will send the screenshot to all contacts listed in "parameter.xlsx" under column A
  It will work For each contact in "contact.xlsx"
  It will send the respective message for a contact from "contact.xlsx" under column D

## The Version 4 will do the following tasks:
  It will work For each contact in "contact.xlsx"
  It will send the respective message for a contact from "contact.xlsx" under column D

## NOTE: 
### 1. For changing the files "contacts.xlsx" and "parameter.xlsx", the directory containing these files are under 
	WhatsApp-BOT\assets\data\contact.xlsx
	WhatsApp-BOT\assets\data\parameter.xlsx

### 2. For changing the "gift.png", the directory containing the image is under
	WhatsApp-BOT\assets\image\gift.png

### 3. For changing the location of any of the following "contacts.xlsx", "parameter.xlsx" or "gift.xlsx"
	you need to change the path to desired path from WhatsApp-BOT\config.py
    Important :- Write the names in contacts.xlsx same as the names saved in your phone contacts
