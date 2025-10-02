from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_dialog_title(browser, timeout=2):
  dialog_overlay = WebDriverWait(browser, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//div[@data-slot='dialog-overlay' and @data-state='open']"))
  )

  dialog = dialog_overlay.find_element(By.XPATH, "./following-sibling::div[@role='dialog']")
  dialog_title = dialog.find_element(By.XPATH, ".//h2")
  return dialog_title.text
