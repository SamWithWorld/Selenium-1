from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class McdonaldsSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.mcdonalds.com/us/en/home.html"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_mcdonalds_search(self):
        driver = self.driver
        driver.get(self.base_url + "/us/en/home.html")
        driver.find_element_by_id("foodnav_link").click()
        driver.find_element_by_link_text("Food").click()
        driver.find_element_by_id("restaurantflyout_link").click()
        driver.find_element_by_id("leftnav_restaurant_text").clear()
        driver.find_element_by_id("leftnav_restaurant_text").send_keys("10017")
        driver.find_element_by_css_selector("input.input_submit_bg").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | _self | 30000]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
