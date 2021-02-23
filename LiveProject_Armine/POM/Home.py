from selenium import webdriver
from selenium.webdriver.common.by import By



class Home:
# page locators
    contact_us      =(By.ID, 'contact-link')
    search_field    =(By.ID, 'search_query_top')
    sign_in         =(By.XPATH, '//div//a[@class="login"]')
    cart            =(By.XPATH, '//div//a[@title="View my shopping cart"]')
    women           =(By.LINK_TEXT, 'Women')
    dresses         =(By.LINK_TEXT, 'Dresses')
    t_shirts        =(By.LINK_TEXT, 'T-shirts')
    product_names   =(By.XPATH, '//a[contains(@class, "product-name")]')
    product_prices  =(By.XPATH, '//span[contains(@class, "price product-price")]')
   
   # page constructor
    def __init__(self, browser):
        self.browser=browser