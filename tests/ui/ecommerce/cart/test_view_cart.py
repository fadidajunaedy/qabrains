from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification

def test_view_cart_page_empty_state(browser, logger):
  logger.info("=== [START] TEST VIEW CART PAGE EMPTY STATE ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.click_cart()
    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[@id='cart']"))
    )
    assert "/cart" in browser.current_url
    assert browser.find_element(By.XPATH, "//h1").text == "Your cart is empty."
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST VIEW CART PAGE EMPTY STATE ===")

def test_view_cart_page_shows_added(browser, logger):
  logger.info("=== [START] TEST VIEW CART PAGE SHOWS ADDED ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.add_to_cart("Sample Shirt Name")
    assert get_notification(browser) == "Added to cart"

    home_page.click_cart()
    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[@id='cart']"))
    )
    assert "/cart" in browser.current_url

    cart = WebDriverWait(browser, 5).until(
      EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'cart-list')]//h3"))
    )
    texts = [product.text for product in cart]
    assert "Sample Shirt Name" in texts, f"Cart list: {texts}"

  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST VIEW CART PAGE SHOWS ADDED ===")

def test_view_cart_page_shows_added_after_refresh(browser, logger):
  logger.info("=== [START] TEST VIEW CART PAGE SHOWS ADDED AFTER REFRESH ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.add_to_cart("Sample Shirt Name")
    assert get_notification(browser) == "Added to cart"

    home_page.click_cart()
    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[@id='cart']"))
    )
    assert "/cart" in browser.current_url

    cart = WebDriverWait(browser, 5).until(
      EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'cart-list')]//h3"))
    )
    texts = [product.text for product in cart]
    assert "Sample Shirt Name" in texts, f"Cart list: {texts}"

    browser.refresh()

    cart = WebDriverWait(browser, 5).until(
      EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'cart-list')]//h3"))
    )
    texts = [product.text for product in cart]
    assert "Sample Shirt Name" in texts, f"Cart list: {texts}"
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST VIEW CART PAGE SHOWS ADDED AFTER REFRESH ===")
