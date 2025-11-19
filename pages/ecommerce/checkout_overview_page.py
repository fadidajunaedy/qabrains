from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.cart_list = (By.XPATH, "//div[contains(@class, 'cart-list')]")
    self.total = (By.XPATH, "//p[starts-with(text(), 'Item Total')]")
    self.tax = (By.XPATH, "//p[starts-with(text(), 'Tax')]")
    self.total_after_tax = (By.XPATH, "//h4[contains(text(), 'Price Total')]/following-sibling::p[starts-with(text(), 'Total')]")
    self.finish_button = (By.XPATH, "//button[span[text()='Finish']]")

  def get_quantity_per_product(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/parent::div/parent::div/following-sibling::div/p[text()='Quantity']/following-sibling::div/span")
    self.logger.info(f"Get product quantity")
    self.logger.debug(f"Locator used: {locator}")
    quantity = cart_list.find_element(*locator)
    return int(quantity.text)

  def get_price_per_product(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/parent::div/parent::div/following-sibling::div/p[text()='Price']/following-sibling::p")
    self.logger.info(f"Get product price")
    self.logger.debug(f"Locator used: {locator}")
    price = cart_list.find_element(*locator)
    return float(price.text.replace("$", ""))

  def get_total_per_product(self, product):
    self.logger.info(f"Accessing cart list")
    self.logger.debug(f"Locator used: {self.cart_list}")
    cart_list = self.driver.find_element(*self.cart_list)

    locator = (By.XPATH, f".//div/div/h3[text()='{product}']/parent::div/parent::div/following-sibling::div/p[text()='Total']/following-sibling::p")
    self.logger.info(f"Get product total price")
    self.logger.debug(f"Locator used: {locator}")
    total = cart_list.find_element(*locator)
    return float(total.text.replace("$", ""))

  def get_total(self):
    self.logger.info("Getting total price")
    self.logger.debug(f"Locator used: {self.total}")
    text = self.driver.find_element(*self.total).text
    total = float(text.split("$")[1])
    return total

  def get_tax(self):
    self.logger.info("Getting tax")
    self.logger.debug(f"Locator used: {self.tax}")
    text = self.driver.find_element(*self.tax).text
    tax = float(text.split("$")[1])
    return tax

  def get_total_after_tax(self):
    self.logger.info("Getting total price after tax")
    self.logger.debug(f"Locator used: {self.total_after_tax}")
    text = self.driver.find_element(*self.total_after_tax).text
    total_after_tax = float(text.split("$")[1])
    return total_after_tax

  def click_finish_button(self):
    self.logger.info("Clicking finish button")
    self.logger.debug(f"Locator used: {self.finish_button}")
    finish_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable(self.finish_button)
    )

    self.driver.execute_script("arguments[0].scrollIntoView('alignToTop');", finish_button)
    finish_button.click()
