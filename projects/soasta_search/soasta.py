from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Soasta(unittest.TestCase):
    def setUp(self):
		# instance of Firefox WebDriver is created
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.soastastore.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_soasta(self):
        driver = self.driver
		# driver.get method navigates to a page given by the URL
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Store").click()
        driver.find_element_by_link_text("Tron: Legacy").click()
        driver.find_element_by_id("product_155_submit_button").click()
        Select(driver.find_element_by_name("product_rating")).select_by_visible_text("2")
        driver.find_element_by_id("s").clear()
        driver.find_element_by_id("s").send_keys("firth")
        driver.find_element_by_id("searchsubmit").click()
        driver.find_element_by_link_text(u"The King’s Speech").click()
        Select(driver.find_element_by_name("product_rating")).select_by_visible_text("4")
        driver.find_element_by_css_selector("form.wpsc_product_rating > input[type=\"submit\"]").click()
        driver.find_element_by_id("product_160_submit_button").click()
        driver.find_element_by_link_text("Checkout").click()
        driver.find_element_by_css_selector("form.adjustform.remove > input[name=\"submit\"]").click()
        driver.find_element_by_css_selector("span > input[name=\"submit\"]").click()
        # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*ERROR: Please enter a username\.[\s\S]*$")
    
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
