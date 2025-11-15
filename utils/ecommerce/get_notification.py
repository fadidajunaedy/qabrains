from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_notification(browser, timeout=5):
  toast = WebDriverWait(browser, timeout).until(
    EC.visibility_of_element_located((By.XPATH, "//li[@data-sonner-toast and @data-visible='true']"))
  )

  toast_title = WebDriverWait(browser, timeout).until(
    EC.visibility_of_element_located((By.XPATH, "//li[@data-sonner-toast and @data-visible='true']//div[@data-title]"))
  )

  notification_message = toast_title.text.strip()
  return notification_message
