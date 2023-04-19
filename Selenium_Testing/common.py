from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def install_extension(extension_path):
    # Set up Chrome options to install extension
    chrome_options = Options()
    chrome_options.add_extension(extension_path)

    # Launch Chrome browser with extension
    driver = webdriver.Chrome(options=chrome_options)

    return driver
