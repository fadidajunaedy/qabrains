from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage
from pages.ecommerce.login_page import LoginPage

def test_login_ecommerce_valid(browser, logger):
  logger.info("=== [START] TEST LOGIN VALID ===")
  try:
    browser.get("https://practice.qabrains.com/ecommerce/login")
    page = LoginPage(browser, logger)
    page.enter_email("test@qabrains.com")
    page.enter_password("Password123")
    page.click_login()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".ecommerce-layout"))
    )

    assert "https://practice.qabrains.com/ecommerce" == browser.current_url

  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN VALID ===")

def test_login_ecommerce_email_invalid(browser, logger):
  logger.info("=== [START] TEST LOGIN EMAIL INVALID ===")
  try:
    browser.get("https://practice.qabrains.com/ecommerce/login")
    page = LoginPage(browser, logger)
    page.enter_email("wrong_email@mail.com")
    page.enter_password("Password123")
    page.click_login()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[text()='Password matched but email is incorrect.']"))
    )

  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN EMAIL INVALID ===")

def test_login_ecommerce_password_invalid(browser, logger):
  logger.info("=== [START] TEST LOGIN PASSWORD INVALID ===")
  try:
    browser.get("https://practice.qabrains.com/ecommerce/login")
    page = LoginPage(browser, logger)
    page.enter_email("test@qabrains.com")
    page.enter_password("wrong_password")
    page.click_login()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[text()='Username matched but password is incorrect.']"))
    )

  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN PASSWORD INVALID ===")

def test_login_ecommerce_invalid(browser, logger):
  logger.info("=== [START] TEST LOGIN INVALID ===")
  try:
    browser.get("https://practice.qabrains.com/ecommerce/login")
    page = LoginPage(browser, logger)
    page.enter_email("wrong_email@mail.com")
    page.enter_password("wrong_password")
    page.click_login()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[text()='Neither email nor password matched.']"))
    )

  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN INVALID ===")

def test_login_ecommerce_valid_then_logout(browser, logger):
  logger.info("=== [START] TEST LOGIN VALID THEN LOGOUT ===")
  try:
    browser.get("https://practice.qabrains.com/ecommerce/login")
    page = LoginPage(browser, logger)
    page.enter_email("test@qabrains.com")
    page.enter_password("Password123")
    page.click_login()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".ecommerce-layout"))
    )

    assert "https://practice.qabrains.com/ecommerce" == browser.current_url

    home_page = HomePage(browser, logger)
    home_page.open_menu_dropdown()
    home_page.click_logout()

    dialog = browser.find_element(By.XPATH, "//div[@role='dialog']")
    assert dialog.find_element(By.XPATH, "//h2[@data-slot='dialog-title']").text == "Are you sure you want to log out?"

    home_page.click_confirmation_logout()

    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".ecommerce-auth-layout"))
    )

    assert "https://practice.qabrains.com/ecommerce/login" == browser.current_url
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN VALID THEN LOGOUT ===")
