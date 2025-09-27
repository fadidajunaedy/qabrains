from selenium.webdriver.common.by import By

class DetailProductPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.favorite_button_toggle = (By.XPATH, "//span[@role='button']/button")
    self.decrease_quantity_button = (By.XPATH, "//button[text()='−']")
    self.increase_quantity_button = (By.XPATH, "//button[text()='+']")
    self.add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
