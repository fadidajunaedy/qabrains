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
