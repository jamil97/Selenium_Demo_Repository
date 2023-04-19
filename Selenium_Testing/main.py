import unittest
import environmental_variables
import HtmlTestRunner
import testApp

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from common import install_extension


# Imported Variables.
crx = environmental_variables.vessel_extension

# Install extension and get the driver object
extension_path = crx

# Uses the "TestCase" sub library included in the "unittest" library.
class GoogleSearchTest(unittest.TestCase):

    # Pre Suite Setup for each individual test case included on the same test suite.
    def setUp(self):
        #Creates a driver instance which initiates a new chrome instance with the indicated extension. 
        self.driver = install_extension(extension_path)

    # Post Suite Teardown for each individual test case included on the same test suite.
    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_google_search(self):
        testApp.google_search(self, self.driver, 'Partner Hero', 'https://www.google.com/')

    def test_website_element(self):
        testApp.open_MockUp_Page(self, self.driver, 'https://www.example.com/')

# Creates a test suite using the "TestSuite" sublibrary from "unittest" and adds the class to it.
# It then runs the tests using the "HTMLTestRunner" and saves the results in an HTML file. (Can be named as wished)
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(GoogleSearchTest))

    runner = HtmlTestRunner.HTMLTestRunner(output='Log')
    runner.run(test_suite)
    