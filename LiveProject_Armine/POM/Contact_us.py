from selenium import webdriver
from selenium.webdriver.common.by import By

class Contact_us:
     # page locators
    subject_heading     =(By.ID, 'id_contact')
    email_address       =(By.ID, 'email')
    order_reference     =(By.ID, 'id_order')
    attach_file         =(By.ID, 'fileUpload')
    send_button         =(By.ID, 'submitMessage')
    message_field       =(By.ID, 'message')


    # page constructor
    def __init__(self, browser):
        self.browser=browser
        