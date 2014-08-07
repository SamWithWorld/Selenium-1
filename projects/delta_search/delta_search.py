from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class DeltaSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.delta.com/index.jsp?Log=1&mkcpgn=SEzzzq1a&s_kwcid=TC|8495|delta||S|e|39374931639&clickid=64336818-6fcf-9b89-ca1a-00005d23aed8&tracking_id=287x119497"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_delta_search(self):
        driver = self.driver
        driver.get(self.base_url + "/index.jsp?Log=1&mkcpgn=SEzzzq1a&s_kwcid=TC|8495|delta||S|e|39374931639&clickid=64336818-6fcf-9b89-ca1a-00005d23aed8&tracking_id=287x119497")
        driver.find_element_by_link_text("Planning a Trip").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Group Travel')])[2]").click()
    
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
