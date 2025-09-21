from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid(browser):
  browser.get("https://practice.qabrains.com")
  page = LoginPage(browser)
  page.enter_email("qa_testers@qabrains.com")
  page.enter_password("Password123")
  page.click_login()

  WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Login Successful']"))
  )

  assert "logged=true" in browser.current_url

def test_login_invalid(browser):
  browser.get("https://practice.qabrains.com")
  page = LoginPage(browser)
  page.enter_email("wrong_email@mail.com")
  page.enter_password("wrong_pass")
  page.click_login()

  WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Your email and password both are invalid!']"))
  )
