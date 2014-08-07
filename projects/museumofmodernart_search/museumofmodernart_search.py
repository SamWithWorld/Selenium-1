from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class MuseumofmodernartSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.moma.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_museumofmodernart_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Buy tickets").click()
        driver.find_element_by_css_selector("img[alt=\"Date\"]").click()
        driver.find_element_by_link_text("27").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "cart_items_tickets_VS.VS0002291.GENERALADM.2014-08-27_ADULT"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_name("commit").click()
    
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
