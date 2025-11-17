from pages.ecommerce.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(browser, logger):
  browser.get("https://practice.qabrains.com/ecommerce/login")
  browser.maximize_window()
  browser.fullscreen_window()
  page = LoginPage(browser, logger)
  page.enter_email("test@qabrains.com")
  page.enter_password("Password123")
  page.click_login()

  WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".ecommerce-layout"))
  )

  assert "https://practice.qabrains.com/ecommerce" == browser.current_url

  return browser
