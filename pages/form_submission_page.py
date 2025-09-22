from selenium.webdriver.common.by import By

class FormSubmissionPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.name_input = (By.XPATH, "//input[@name='name']")
    self.email_input = (By.XPATH, "//input[@name='email']")
    self.contact_input = (By.XPATH, "//input[@name='contact']")
    self.date_input = (By.XPATH, "//input[@type='date' and @name='date']")
    self.file_input = (By.XPATH, "//input[@type='file' and @name='file']")
    self.color_select = (By.XPATH, "//label[@for='color']/following-sibling::div/div")
    self.food_select = (By.XPATH, "//label[@for='food']/following-sibling::div/div")
    self.country_select = (By.XPATH, "//select[@name='country']")
    self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")

  def enter_name(self, name):
    self.logger.info("Input name")
    self.logger.debug(f"Locator used: {self.name_input}")
    self.driver.find_element(*self.name_input).send_keys(name)

  def enter_email(self, email):
    self.logger.info("Input email")
    self.logger.debug(f"Locator used: {self.email_input}")
    self.driver.find_element(*self.email_input).send_keys(email)

  def enter_contact(self, contact):
    self.logger.info("Input contact")
    self.logger.debug(f"Locator used: {self.contact_input}")
    self.driver.find_element(*self.contact_input).send_keys(contact)

  def enter_date(self, date):
    self.logger.info("Input date")
    self.logger.debug(f"Locator used: {self.date_input}")
    self.driver.find_element(*self.date_input).send_keys(date)

  def enter_file(self, file):
    self.logger.info("Input file")
    self.logger.debug(f"Locator used: {self.file_input}")
    self.driver.find_element(*self.file_input).send_keys(file)

  def enter_color(self, color):
    self.logger.info("Input color")
    self.logger.debug(f"Locator used: {self.color_select}")
    group_color = self.driver.find_element(*self.color_select)
    group_color.find_element(By.XPATH, f"//label[@for='{color}']").click()

  def enter_food(self, food):
    self.logger.info("Input food")
    self.logger.debug(f"Locator used: {self.food_select}")
    group_food = self.driver.find_element(*self.food_select)
    group_food.find_element(By.XPATH, f"//label[@for='{food}']").click()

  def enter_country(self, country):
    self.logger.info("Select country")
    self.logger.debug(f"Locator used: {self.country_select}")

    select = self.driver.find_element(*self.country_select)
    select.find_element(By.XPATH, f"//option[@value='{country}']").click()

  def click_submit(self):
    self.logger.info("Click submit button")
    self.logger.debug(f"Locator used: {self.submit_button}")
    self.driver.find_element(*self.submit_button).click()
