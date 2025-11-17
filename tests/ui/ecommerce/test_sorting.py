from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage

from utils.ecommerce.login import login

def test_sorting_product_by_ascending(browser, logger):
  logger.info("=== [START] TEST SORTING PRODUCT BY ASCENDING ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.click_sorting_list_button()
    home_page.click_sorting_framework("A to Z (Ascending)")
    WebDriverWait(browser, 5).until(EC.url_contains("order_by=asc"))
    assert "order_by=asc" in browser.current_url

    products = browser.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div")
    first_product = browser.find_element(By.XPATH, "//div[contains(@class, 'products')]/div[1]/a[2]")
    last_product = browser.find_element(By.XPATH, "//div[contains(@class, 'products')]/div[last()]/a[2]")
    assert first_product.text < last_product.text
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST SORTING PRODUCT BY ASCENDING ===")

def test_sorting_product_by_descending(browser, logger):
  logger.info("=== [START] TEST SORTING PRODUCT BY DESCENDING ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.click_sorting_list_button()
    home_page.click_sorting_framework("Z to A (Descending)")
    WebDriverWait(browser, 5).until(EC.url_contains("order_by=dsc"))
    assert "order_by=dsc" in browser.current_url

    products = browser.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div")
    first_product = browser.find_element(By.XPATH, "//div[contains(@class, 'products')]/div[1]/a[2]")
    last_product = browser.find_element(By.XPATH, "//div[contains(@class, 'products')]/div[last()]/a[2]")
    assert first_product.text > last_product.text
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST SORTING PRODUCT BY DESCENDING ===")

def test_sorting_product_by_low_price(browser, logger):
  logger.info("=== [START] TEST SORTING PRODUCT BY LOW PRICE ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.click_sorting_list_button()
    home_page.click_sorting_framework("Low to High (Price)")
    WebDriverWait(browser, 5).until(EC.url_contains("order_by=low"))
    assert "order_by=low" in browser.current_url

    products = browser.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div")
    first_product = browser.find_element(By.XPATH, "//div[contains(@class, 'products')]/div[1]/div/span")
    last_product = browser.find_element(By.XPATH, "//div[contains(@class, 'products')]/div[last()]/div/span")
    assert float(first_product.text.replace("$", "")) < float(last_product.text.replace("$", ""))
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST SORTING PRODUCT BY LOW PRICE ===")

def test_sorting_product_by_high_price(browser, logger):
  logger.info("=== [START] TEST SORTING PRODUCT BY HIGH PRICE ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.click_sorting_list_button()
    home_page.click_sorting_framework("High to Low (Price)")
    WebDriverWait(browser, 5).until(EC.url_contains("order_by=high"))
    assert "order_by=high" in browser.current_url

    products = browser.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div")
    first_product = browser.find_element(By.XPATH, "//div[contains(@class, 'products')]/div[1]/div/span")
    last_product = browser.find_element(By.XPATH, "//div[contains(@class, 'products')]/div[last()]/div/span")
    assert float(first_product.text.replace("$", "")) > float(last_product.text.replace("$", ""))
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST SORTING PRODUCT BY HIGH PRICE ===")
