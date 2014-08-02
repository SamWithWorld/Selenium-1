from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class AmazonSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.amazon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_amazon_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("twotabsearchtextbox").click()
        driver.find_element_by_id("twotabsearchtextbox").clear()
        driver.find_element_by_id("twotabsearchtextbox").send_keys("samsung galaxy s5")
        driver.find_element_by_css_selector("input.nav-submit-input").click()
        driver.find_element_by_css_selector("span.lrg.bold").click()
        # Hovers over the image
        driver.find_element_by_id("dp").click()
        driver.find_element_by_id("dp").click()
        driver.find_element_by_id("dp").click()
        driver.find_element_by_id("twotabsearchtextbox").clear()
        driver.find_element_by_id("twotabsearchtextbox").send_keys("")
        driver.find_element_by_link_text("All Electronics").click()
        driver.find_element_by_css_selector("img[alt=\"Video Games\"]").click()
        driver.find_element_by_xpath("//ul[@id='ref_11846801']/li[3]/a/span").click()
        driver.find_element_by_id("twotabsearchtextbox").clear()
        driver.find_element_by_id("twotabsearchtextbox").send_keys("grand theft auto 5")
        driver.find_element_by_css_selector("input.nav-submit-input").click()
    
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
