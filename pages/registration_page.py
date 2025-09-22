from selenium.webdriver.common.by import By

class RegistrationPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.name_input = (By.XPATH, "//input[@name='name']")
    self.country_select = (By.XPATH, "//select[@name='country']")
    self.account_select = (By.XPATH, "//select[@name='account']")
    self.email_input = (By.XPATH, "//input[@name='email']")
    self.password_input = (By.XPATH, "//input[@type='password' and @name='password']")
    self.confirm_password_input = (By.XPATH, "//input[@type='password' and @name='confirm_password']")
    self.registration_button = (By.CSS_SELECTOR, "button[type='submit']")

  def enter_name(self, name):
    self.logger.info("Input name")
    self.logger.debug(f"Locator used: {self.name_input}")
    self.driver.find_element(*self.name_input).send_keys(name)

  def enter_country(self, country):
    self.logger.info("Select country")
    self.logger.debug(f"Locator used: {self.country_select}")

    select = self.driver.find_element(*self.country_select)
    select.find_element(By.XPATH, f"//option[@value='{country}']").click()

  def enter_account(self, account):
    self.logger.info("Select account")
    self.logger.debug(f"Locator used: {self.account_select}")

    select = self.driver.find_element(*self.account_select)
    select.find_element(By.XPATH, f"//option[@value='{account}']").click()

  def enter_email(self, email):
    self.logger.info("Input email")
    self.logger.debug(f"Locator used: {self.email_input}")
    self.driver.find_element(*self.email_input).send_keys(email)

  def enter_password(self, password):
    self.logger.info("Input password")
    self.logger.debug(f"Locator used: {self.password_input}")
    self.driver.find_element(*self.password_input).send_keys(password)

  def enter_confirm_password(self, confirm_password):
    self.logger.info("Input confirm_password")
    self.logger.debug(f"Locator used: {self.confirm_password_input}")
    self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

  def click_registration(self):
    self.logger.info("Click registration button")
    self.logger.debug(f"Locator used: {self.registration_button}")
    self.driver.find_element(*self.registration_button).click()
