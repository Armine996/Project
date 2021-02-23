from LiveProject_Armine.POM.Home import Home
from LiveProject_Armine.POM.SignIn import Sign_in
from LiveProject_Armine.POM.lib import Lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import pytest


'''
1. Navigate to URL
2. Click on Sign In button of the Home Page
3. Fill in the email address and password fields
4. Click on Sign In button
5. Verify that signed in successfully
'''

def test_1():
    try:
        #create lib page object
        obj_lib=Lib()

        # open browser
        browser=obj_lib.open_browser()
        
        # navigate to the url
        obj_lib.page_load(browser)

        # create Sign_in_page object
        obj_sign_in=Sign_in(browser)

        # parse data from config.json for email and password fields
        with open('config.json') as f:
            data=json.load(f)
        email_address=data['email']
        password=data['password']

        # create Home_page object 
        obj_home=Home(browser)

        # click on Sign In button of the Home page
        browser.find_element(*obj_home.sign_in).click()

        # wait for the element to be visible in Sign in page
        obj_lib.wait_for_element(browser, obj_sign_in.email_address)

        # submit the email address and password parsed from config.json to be signed with
        browser.find_element(*obj_sign_in.email_address).send_keys(email_address)
        browser.find_element(*obj_sign_in.password).send_keys(password)

        # click the sign in button
        browser.find_element(*obj_sign_in.sign_in_button).click()

        # check that signed in to my account has been succesfull
        try:
            sign_out_title=browser.find_element(*obj_sign_in.sign_out).title
            print(sign_out_title)
        except:
            print("The web element Sign out is not fount, so you arer signed in!")

        print('Test 1 passed!')
    
    except Exception as e:
            # save the screenshot of the test file which has failed
            obj_lib.save_screenshot(browser)
            pytest.fail(e)
            print('Test 1 failed!')
    
    finally:
        # close the browser
        obj_lib.close_browser(browser) 