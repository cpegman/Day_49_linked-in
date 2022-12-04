from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from data.creds import pw, user


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

username.send_keys(user)
password.send_keys(pw)
sign_in.click()

# job_desc = input("what job")
location = "Cincinnatti"

driver.find_element(By.LINK_TEXT, "Jobs").click()
job_search_box = driver.find_element(
    By.CSS_SELECTOR, 'input[id*="jobs-search-box-keyword"]'
)
job_search_box.send_keys("python developer")
job_search_box.send_keys(Keys.ENTER)

loc_search_box = driver.find_element(
    By.CSS_SELECTOR, 'input[id*="jobs-search-box-location"]'
)
loc_search_box.clear()
time.sleep(1)
loc_search_box.send_keys(location)
loc_search_box.send_keys(Keys.ENTER)

easy_apply_button = driver.find_element(
    By.CSS_SELECTOR, 'button[aria-label*="Easy Apply"]'
).click()
search_button = driver.find_element(
    By.CSS_SELECTOR, 'button[class*="jobs - search - box__submit"]'
)
search_button.click()


search_button.click()
