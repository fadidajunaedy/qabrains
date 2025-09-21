from selenium.webdriver.common.by import By
from utils.logger import get_logger
logger = get_logger()

class LoginPage:
  def __init__(self, driver):
    self.driver = driver
    self.email_input = (By.ID, "email")
    self.password_input = (By.ID, "password")
    self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

  def enter_email(self, email):
    logger.info("Input email")
    logger.debug(f"Locator used: {self.email_input}")
    self.driver.find_element(*self.email_input).send_keys(email)

  def enter_password(self, password):
    logger.info("Input password")
    logger.debug(f"Locator used: {self.password_input}")
    self.driver.find_element(*self.password_input).send_keys(password)

  def click_login(self):
    logger.info("Click login button")
    logger.debug(f"Locator used: {self.login_button}")
    self.driver.find_element(*self.login_button).click()
