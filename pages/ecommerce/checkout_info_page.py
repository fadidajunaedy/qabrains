from selenium.webdriver.common.by import By

class CheckoutInfoPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.first_name_input = (By.XPATH, "//div[@class='form-group']/label[text()='First Name']/following-sibling::input")
    self.last_name_input = (By.XPATH, "//div[@class='form-group']/label[text()='Last Name']/following-sibling::input")
    self.zip_code_input = (By.XPATH, "//div[@class='form-group']/label[text()='Zip Code']/following-sibling::input")
    self.continue_button = (By.XPATH, "//button[span[text()='Continue']]")

  def enter_first_name(self, first_name):
    self.logger.info("Input first name")
    self.logger.debug(f"Locator used: {self.first_name_input}")
    self.driver.find_element(*self.first_name_input).send_keys(first_name)

  def enter_last_name(self, last_name):
    self.logger.info("Input last name")
    self.logger.debug(f"Locator used: {self.last_name_input}")
    self.driver.find_element(*self.last_name_input).send_keys(last_name)

  def enter_zip_code(self, zip_code):
    self.logger.info("Input zip code")
    self.logger.debug(f"Locator used: {self.zip_code_input}")
    zip_code_input = self.driver.find_element(*self.zip_code_input)
    zip_code_input.clear()
    zip_code_input.send_keys(zip_code)

  def click_continue_button(self):
    self.logger.info("Clicking continue button")
    self.logger.debug(f"Locator used: {self.continue_button}")
    self.driver.find_element(*self.continue_button).click()
