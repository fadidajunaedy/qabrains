from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
logger = get_logger()

def test_login_valid(browser):
  logger.info("=== [START] TEST LOGIN VALID ===")
  try:
    browser.get("https://practice.qabrains.com")
    page = LoginPage(browser)
    page.enter_email("qa_testers@qabrains.com")
    page.enter_password("Password123")
    page.click_login()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//span[text()='Login Successful']"))
    )

    assert "logged=true" in browser.current_url
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN VALID ===")

def test_login_invalid(browser):
  logger.info("=== [START] TEST LOGIN INVALID ===")
  try:
    browser.get("https://practice.qabrains.com")
    page = LoginPage(browser)
    page.enter_email("wrong_email@mail.com")
    page.enter_password("wrong_pass")
    page.click_login()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//span[text()='Your email and password both are invalid!']"))
    )

    assert "email=false&password=false" in browser.current_url
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN INVALID ===")
