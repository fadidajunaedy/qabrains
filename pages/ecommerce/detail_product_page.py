from selenium.webdriver.common.by import By

class DetailProductPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.favorite_button_toggle = (By.XPATH, "//span[@role='button']/button")
    self.decrease_quantity_button = (By.XPATH, "//button[text()='−']")
    self.increase_quantity_button = (By.XPATH, "//button[text()='+']")
    self.add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")

  def increase_quantity_product(self):
    self.logger.info("Clicking increase quantity button")
    self.logger.debug(f"Locator used: {self.increase_quantity_button}")
    increase_button = self.driver.find_element(*self.increase_quantity_button)
    increase_button.click()

  def decrease_quantity_product(self):
    self.logger.info("Clicking decrease quantity button")
    self.logger.debug(f"Locator used: {self.decrease_quantity_button}")
    decrease_button = self.driver.find_element(*self.decrease_quantity_button)
    decrease_button.click()

  def add_product_to_cart(self):
    self.logger.info("Clicking add to cart button")
    self.logger.debug(f"Locator used: {self.add_to_cart_button}")
    self.driver.find_element(*self.add_to_cart_button).click()
