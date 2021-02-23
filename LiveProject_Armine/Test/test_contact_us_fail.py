from LiveProject_Armine.POM.Home import Home
from LiveProject_Armine.POM.SignIn import Sign_in
from LiveProject_Armine.POM.lib import Lib
from LiveProject_Armine.POM.Contact_us import Contact_us
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json
import pytest


'''
1. Navigate to the URL
2. Click Contact Us button
3. Fill in all the fields in Contact us page besides Message field
4. Click on the Send button
4. Verify that the validation message has appeared
5. Close the browser
'''
def test_3():

        try:  
            # create lib page object  
            obj_lib=Lib()

            # open browser
            browser=obj_lib.open_browser()

            # navigate to the url
            obj_lib.page_load(browser)

            #create Home and Contact_us pages objects
            obj_home=Home(browser)
            obj_contact_us=Contact_us(browser)

            # click on Sign In button of the Home page
            browser.find_element(*obj_home.contact_us).click()

            # wait for the element to be visible in Sign in page
            obj_lib.wait_for_element(browser, obj_contact_us.subject_heading)

            # locate subject heading element and choose one of the options
            element = browser.find_element(*obj_contact_us.subject_heading)
            element.click()
            select_text = obj_lib.get_data(key='subject_heading')
            select_option = Select(element)
            select_option.select_by_visible_text(select_text)

            # fill in the email field
            valid_email_value=obj_lib.get_data(key='valid_email')
            browser.find_element(*obj_contact_us.email_address).send_keys(valid_email_value)

            # input in order reference field
            order_reference_value=obj_lib.get_data(key='references')
            browser.find_element(*obj_contact_us.order_reference).send_keys(order_reference_value)

            # click Send button
            browser.find_element(*obj_contact_us.send_button).click()

            # validate that error message has appeared
            error_message=obj_lib.get_data(key='contact_us_error_message') 
            assert error_message in browser.page_source
            print("Test 3 passed!")

        except Exception as e:
            # save the screenshot of the test file which has failed
            obj_lib.save_screenshot(browser)
            pytest.fail(e)
            print('Test 3 failed!')
    
        finally:
            # close the browser
            obj_lib.close_browser(browser)  