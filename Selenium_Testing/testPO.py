import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import install_extension

#Page Objects contain the general logic for all methods. 
#Using a page object will allow us to reuse keywords for different tests as well as keeping the code cleaner and organized. 

def open_Website(self, driver, web_page):
      self.driver.get(web_page)

def google_search(self, driver, text):
    # Wait for search box to load
    wait = WebDriverWait(self.driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))

    # Enter a search query
    search_box.send_keys(text)

    # Submit the search query
    search_box.submit()
    time.sleep(5)

    # Verify that search results page is loaded
    self.assertTrue(text in self.driver.title)

def verify_Page_Elements(self, driver):
        # Wait for element to load
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'img')))

        # Verify that the element is present on the page
        self.assertTrue(element.is_displayed())