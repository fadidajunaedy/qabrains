from selenium.webdriver.common.by import By

class DetailPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.favorite_toggle_button = (By.XPATH, "//span[@role='button']/button")
    self.quantity_input = (By.XPATH, "//input[@readonly]")
    self.decrease_quantity_button = (By.XPATH, "//button[text()='−']")
    self.increase_quantity_button = (By.XPATH, "//button[text()='+']")
    self.add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")

  def toggling_favorite(self):
    self.logger.info("Clicking Add to favorite button")
    self.logger.debug(f"Locator used: {self.favorite_toggle_button}")
    self.driver.find_element(*self.favorite_toggle_button).click()

  def get_quantity(self):
    self.logger.info("Getting quantity")
    self.logger.debug(f"Locator used: {self.quantity_input}")
    return int(self.driver.find_element(*self.quantity_input).get_attribute("value"))

  def increase_quantity(self):
    self.logger.info("Clicking increase quantity button")
    self.logger.debug(f"Locator used: {self.increase_quantity_button}")
    increase_button = self.driver.find_element(*self.increase_quantity_button)
    increase_button.click()

  def decrease_quantity(self):
    self.logger.info("Clicking decrease quantity button")
    self.logger.debug(f"Locator used: {self.decrease_quantity_button}")
    decrease_button = self.driver.find_element(*self.decrease_quantity_button)
    decrease_button.click()

  def add_to_cart(self):
    self.logger.info("Clicking add to cart button")
    self.logger.debug(f"Locator used: {self.add_to_cart_button}")
    self.driver.find_element(*self.add_to_cart_button).click()
