from selenium import webdriver
from selenium.webdriver.common.by import By


class Sign_in:

    # page locators
    email_address       =(By.ID, "email")
    password            =(By.ID, "passwd")
    sign_in_button      =(By.ID, "SubmitLogin")
    my_account_title    =(By.XPATH, "//h1[text()='My account']")
    sign_out            =(By.LINK_TEXT, "Sign out")
    
    # page constructor
    def __init__(self, browser):
        self.browser=browser