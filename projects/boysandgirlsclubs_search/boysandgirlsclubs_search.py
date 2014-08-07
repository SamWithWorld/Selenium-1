from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class BoysandgirlsclubsSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.bgca.org/Pages/index.aspx"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_boysandgirlsclubs_search(self):
        driver = self.driver
        driver.get(self.base_url + "/Pages/index.aspx")
        driver.find_element_by_link_text("Mission").click()
        driver.find_element_by_css_selector("input.zip").click()
        driver.find_element_by_css_selector("input.zip").clear()
        driver.find_element_by_css_selector("input.zip").send_keys("10000")
        driver.find_element_by_css_selector("a.FindAClubButton > img").click()
    
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
