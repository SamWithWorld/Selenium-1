from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class NikeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.nike.com/us/en_us/c/jordan/derek-jeter-re2pect"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_nike_search(self):
        driver = self.driver
        driver.get(self.base_url + "/us/en_us/c/jordan/derek-jeter-re2pect")
        driver.find_element_by_name("searchList").click()
        driver.find_element_by_xpath("//span[3]").click()
        driver.find_element_by_name("searchList").clear()
        driver.find_element_by_name("searchList").send_keys("re2pect")
    
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
