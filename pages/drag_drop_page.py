from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragDropPage:
  def __init__(self, driver, logger):
    self.driver = driver
    self.logger = logger
    self.drag_element = (By.XPATH, "//div[@draggable='true' and text()='Drag Me']")
    self.drop_area_element = (By.XPATH, "//div[text()='Drop Here']")

  def drag_and_drop(self):
    self.logger.info("Dragging element")
    self.logger.debug(f"Locator used: {self.drag_element}")
    self.logger.info("Dropping to element")
    self.logger.debug(f"Locator used: {self.drop_area_element}")

    drag_element = self.driver.find_element(*self.drag_element)
    drag_area_element = self.driver.find_element(*self.drop_area_element)
    actions = ActionChains(self.driver)
    actions.drag_and_drop(drag_element, drag_area_element).perform()
