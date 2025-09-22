from pages.drag_drop_page import DragDropPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_drag_drop(browser, logger):
  logger.info("=== [START] TEST DRAG DROP ===")
  try:
    browser.get("https://practice.qabrains.com/drag-drop")
    page = DragDropPage(browser, logger)
    page.drag_and_drop()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[text()='Drag Me']/preceding-sibling::h3"))
    )

    assert browser.find_element(By.XPATH, "//div[text()='Drag Me']/preceding-sibling::h3").text == "Dropped!"
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST DRAG DROP ===")
