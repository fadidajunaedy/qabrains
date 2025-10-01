from selenium.webdriver.common.by import By

class FavoritesPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.products = (By.XPATH, "//div[contains(@class,'products')]") #products grid / container
    self.favorite_toggle_button = (By.XPATH, ".//span[@role='button']/button") # .// meaning relative to product selected
    self.add_to_cart_button = (By.XPATH, ".//button[text()='Add to cart']") # .// meaning relative to product selected
    self.remove_from_cart_button = (By.XPATH, ".//button[text()='Remove from cart']") # meaning relative to product selected

  def get_product(self, product):
    locator = (By.XPATH, f"//div[contains(@class,'products')]//a[text()='{product}']/parent::div")
    self.logger.info("Get product item")
    self.logger.debug(f"Locator used: {locator}")
    return self.driver.find_element(*locator)

  def toggling_favorite(self, product_name):
    product = self.get_product(product_name)
    self.logger.info("Clicking Add to favorite button")
    self.logger.debug(f"Locator used: {self.favorite_toggle_button}")
    product.find_element(*self.favorite_toggle_button).click()

  def add_to_cart(self, product_name):
    product = self.get_product(product_name)
    self.logger.info("Clicking Add to cart button")
    self.logger.debug(f"Locator used: {self.add_to_cart_button}")
    product.find_element(*self.add_to_cart_button).click()

  def remove_from_cart(self, product_name):
    product = self.get_product(product_name)
    self.logger.info("Clicking Remove from cart button")
    self.logger.debug(f"Locator used: {self.remove_from_cart_button}")
    product.find_element(*self.remove_from_cart_button).click()

  def click_product(self, product):
    self.logger.info(f"Accessing products container {product}")
    self.logger.debug(f"Locator used: {self.products}")
    products = self.driver.find_element(*self.products)

    product_locator = (By.XPATH, f".//div/a[text()='{product}']")
    self.logger.info(f"Clicking product {product}")
    self.logger.debug(f"Locator used: {product_locator}")
    products.find_element(*product_locator).click()

