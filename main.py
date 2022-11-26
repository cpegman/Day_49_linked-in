from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class New_driver2(webdriver.Chrome):
    def __init__(self, teardown=False, headless=False, implicitly_wait=20):
        self.teardown = teardown
        self.options = Options()
        if headless:
            self.options.headless = True
            self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
            print("running in headless mode")
        super(New_driver2, self).__init__(
            options=self.options, service=Service(ChromeDriverManager().install())
        )
        self.maximize_window()
        self.implicitly_wait(implicitly_wait)
        self.teardown = teardown

    def __exit__(self, *args):
        if self.teardown:
            print("tearing down session")
            self.quit()


driver = New_driver2()

driver.get("https://www.linkedin.com/")
username = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")
sign_in = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
