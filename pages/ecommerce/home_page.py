from selenium.webdriver.common.by import By

class HomePage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.cart_link_button = (By.XPATH, "//div[contains(@class, 'profile')]//span[@role='button']")
    self.dropdown_menu_trigger = (By.XPATH, "//button[@data-slot='dropdown-menu-trigger']")
    self.dropdown_menu = (By.XPATH, "//div[@data-slot='dropdown-menu-content']")
    self.favorites_link_button = (By.XPATH, "//div[@data-slot='dropdown-menu-item' and normalize-space(text())='Favorites']")
    self.logout_button = (By.XPATH, "//div[@data-slot='dropdown-menu-item' and normalize-space(text())='Log out']")
    self.logout_confirmation_button = (By.XPATH, "//button[@data-slot='dialog-close' and text()='Logout']")
    self.popover_sorting_trigger = (By.XPATH, "//button[@data-slot='popover-trigger']")
    self.search_sorting_framework_input = (By.XPATH, "//input[@data-slot='command-input']")
    self.sorting_group = (By.XPATH, "//div[@data-slot='command-group']")
    self.products = (By.XPATH, "//div[contains(@class,'products')]") #products grid / container
    self.favorite_toggle_button = (By.XPATH, ".//span[@role='button']/button") # .// meaning relative to product selected
    self.add_to_cart_button = (By.XPATH, ".//button[text()='Add to cart']") # .// meaning relative to product selected
    self.remove_from_cart_button = (By.XPATH, ".//button[text()='Remove from cart']") # meaning relative to product selected

  def click_cart(self):
    self.logger.info("Clicking cart link button")
    self.logger.debug(f"Locator used: {self.cart_link_button}")
    self.driver.find_element(*self.cart_link_button).click()

  def get_product(self, product):
    locator = (By.XPATH, f"//div[contains(@class,'products')]//a[text()='{product}']/parent::div/parent::div")
    self.logger.info("Get product item")
    self.logger.debug(f"Locator used: {locator}")
    return self.driver.find_element(*locator)

  def open_menu_dropdown(self):
    self.logger.info("Open the dropdown menu")
    self.logger.debug(f"Locator used: {self.dropdown_menu_trigger}")
    self.driver.find_element(*self.dropdown_menu_trigger).click()

  def click_favorites(self):
    self.driver.find_element(*self.favorites_link_button).click()

  def click_logout(self):
    self.logger.info("Clicking logout button")
    self.logger.debug(f"Locator used: {self.logout_button}")
    self.driver.find_element(*self.logout_button).click()

  def click_confirmation_logout(self):
    self.logger.info("Clicking logout confirmation button")
    self.logger.debug(f"Locator used: {self.logout_confirmation_button}")
    self.driver.find_element(*self.logout_confirmation_button).click()

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



