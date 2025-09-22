from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid(browser, logger):
  logger.info("=== [START] TEST LOGIN VALID ===")
  try:
    browser.get("https://practice.qabrains.com")
    page = LoginPage(browser, logger)
    page.enter_email("qa_testers@qabrains.com")
    page.enter_password("Password123")
    page.click_login()

    success_message = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.ID, "success-msg"))
    )

    assert success_message.find_element(By.TAG_NAME, "h2").text == "LOGIN SUCCESSFUL"
    assert "logged=true" in browser.current_url
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN VALID ===")

def test_login_invalid(browser, logger):
  logger.info("=== [START] TEST LOGIN INVALID ===")
  try:
    browser.get("https://practice.qabrains.com")
    page = LoginPage(browser, logger)
    page.enter_email("wrong_email@mail.com")
    page.enter_password("wrong_pass")
    page.click_login()

    toaster = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "div.toaster"))
    )

    assert toaster.find_element(By.CSS_SELECTOR, "span.title").text == "Your email and password both are invalid!"
    assert "email=false&password=false" in browser.current_url
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST LOGIN INVALID ===")
