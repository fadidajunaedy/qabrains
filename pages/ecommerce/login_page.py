from selenium.webdriver.common.by import By

class LoginPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.email_input = (By.ID, "email")
    self.password_input = (By.ID, "password")
    self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

  def enter_email(self, email):
    self.logger.info("Input email")
    self.logger.debug(f"Locator used: {self.email_input}")
    self.driver.find_element(*self.email_input).send_keys(email)

  def enter_password(self, password):
    self.logger.info("Input password")
    self.logger.debug(f"Locator used: {self.password_input}")
    self.driver.find_element(*self.password_input).send_keys(password)

  def click_login(self):
    self.logger.info("Click login button")
    self.logger.debug(f"Locator used: {self.login_button}")
    self.driver.find_element(*self.login_button).click()
