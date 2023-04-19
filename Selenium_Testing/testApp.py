import testPO
from selenium.webdriver.support import expected_conditions as EC

#The apps are a bridge between the page objects and the test suites.
#They will allow us to create methods that can be reused on any test suite if they contain the same workflow logic.

from common import install_extension

def google_search(self, driver, text, web_page):
    testPO.open_Website(self, driver, web_page)
    testPO.google_search(self, driver, text)

def open_MockUp_Page(self, driver, webpage):
    testPO.open_Website(self, driver, webpage)
    testPO.verify_Page_Elements(self, driver)