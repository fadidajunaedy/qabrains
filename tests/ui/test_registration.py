from pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
logger = get_logger()

def test_registration_valid(browser):
  logger.info("=== [START] TEST REGISTRATION VALID ===")
  try:
    browser.get("https://practice.qabrains.com/registration")
    page = RegistrationPage(browser)
    page.enter_name("Fadida Zanetti Junaedy")
    page.enter_country("Indonesia")
    page.enter_account("Engineer")
    page.enter_email("fadidajunaedy@gmail.com")
    page.enter_password("Password123")
    page.enter_confirm_password("Password123")
    page.click_registration()

    success_message = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.ID, "success-msg"))
    )

    assert success_message.find_element(By.TAG_NAME, "h2").text == "REGISTRATION SUCCESSFUL"
    assert "registered=true" in browser.current_url
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST REGISTRATION VALID ===")
