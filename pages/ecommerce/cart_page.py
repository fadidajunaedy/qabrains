from selenium.webdriver.common.by import By

class CartPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.cart_list = (By.XPATH, "//div[contains(@class, 'cart-list')]")
    self.confirmation_remove_button = (By.XPATH, "//div[@data-slot='dialog-overlay' and @data-state='open']/following-sibling::div[@role='dialog']//button[text()='Remove']")

  def get_quantity(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/parent::div/parent::div/following-sibling::div/p[text()='Quantity']/following-sibling::div/span")
    self.logger.info(f"Get product quantity")
    self.logger.debug(f"Locator used: {locator}")
    quantity = cart_list.find_element(*locator)
    return int(quantity.text)

  def get_price(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/parent::div/parent::div/following-sibling::div/p[text()='Price']/following-sibling::p")
    self.logger.info(f"Get product price")
    self.logger.debug(f"Locator used: {locator}")
    price = cart_list.find_element(*locator)
    return float(price.text.replace("$", ""))

  def get_total(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/parent::div/parent::div/following-sibling::div/p[text()='Total']/following-sibling::p")
    self.logger.info(f"Get product total price")
    self.logger.debug(f"Locator used: {locator}")
    total = cart_list.find_element(*locator)
    return float(total.text.replace("$", ""))

  def click_remove(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/following-sibling::button[text()='Remove']")
    self.logger.info(f"Clicking remove button")
    self.logger.debug(f"Locator used: {locator}")
    cart_list.find_element(*locator).click()

  def click_confirmation_remove(self):
    self.logger.info(f"Clicking confirmation remove button")
    self.logger.debug(f"Locator used: {self.confirmation_remove_button}")
    self.driver.find_element(*self.confirmation_remove_button).click()

  def click_decrease_quantity(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/parent::div/parent::div/following-sibling::div/p[text()='Quantity']/following-sibling::div/button[text()='-']")
    self.logger.info(f"Clicking decrease button")
    self.logger.debug(f"Locator used: {locator}")
    cart_list.find_element(*locator).click()

  def click_increase_quantity(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/parent::div/parent::div/following-sibling::div/p[text()='Quantity']/following-sibling::div/button[text()='+']")
    self.logger.info(f"Clicking increase button")
    self.logger.debug(f"Locator used: {locator}")
    cart_list.find_element(*locator).click()
