""" This program tests to see how long it takes for NBA.com to load from 
Google's search engine """

""" 1. selenium.webdriver module providing  
all the WebDriver implementations
2. "Keys" class provides keys in keyboard
like RETURN, F1, ALT, etc... """

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleComSearch(unittest.TestCase):

	def setUp(self):
		# instance of Firefox WebDriver is created
		self.driver = webdriver.Firefox()

	def test_search_in_google_com(self):
		driver = self.driver
		# driver.get method navigates to a page given by the URL
		driver.get("http://www.google.com")
		# asseration to confirm that the title has "Google" word in it
		self.assertIn("Google", driver.title)
		""" input text element located by its name, "q", attribute using 
		"find_element_by_name" method """
		elem = driver.find_element_by_name("q")
		""" 1. sending keys, similar to entering keys using a keyboard
		2. special keys can be sent using "Keys" class imported
		from "selenium.webdriver.common.keys" """
		elem.send_keys("NBA.com")
		elem.send_keys(Keys.RETURN)

	def tearDown(self):
	""" 1. browser window is closed
	 2. can also call "quit" method instead of "close"
	 3. "quit" exists entire browser
	 4. "close" will close one tab, but if its just one tab,
	 		browser exits entirely by itself """
		self.driver.close()

# provides a command-line interface to the test script
if __name__ == "__main__":
	unittest.main()