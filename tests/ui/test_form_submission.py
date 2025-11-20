import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.form_submission_page import FormSubmissionPage

def test_form_submission_valid(browser, logger):
  logger.info("=== [START] TEST FORM SUBMISSION VALID ===")
  try:
    browser.get("https://practice.qabrains.com/form-submission")
    browser.maximize_window()
    browser.fullscreen_window()
    page = FormSubmissionPage(browser, logger)
    page.enter_name("Fadida Zanetti Junaedy")
    page.enter_email("fadidajunaedy@gmail.com")
    page.enter_contact("089501437800")
    page.enter_date("2025-09-16")
    page.enter_file(os.path.abspath("assets/dummy.png"))
    page.enter_color("Red")
    page.enter_food("Pasta")
    page.enter_country("Indonesia")
    page.click_submit()

    success_message = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.ID, "success-msg"))
    )

    assert success_message.find_element(By.TAG_NAME, "h2").text == "SUCCESSFULLY SUBMITTED"
    assert "submitted=true" in browser.current_url
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST FORM SUBMISSION VALID ===")
