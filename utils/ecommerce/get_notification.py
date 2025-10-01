from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_notification(browser, timeout=2):
  notifications_section = WebDriverWait(browser, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@aria-label, 'Notifications')]"))
  )
  notification_message = notifications_section.find_element(By.XPATH, ".//ol/li/div/div")
  return notification_message.text
