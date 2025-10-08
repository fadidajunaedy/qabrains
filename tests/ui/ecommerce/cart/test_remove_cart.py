from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage
from pages.ecommerce.cart_page import CartPage

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification
from utils.ecommerce.get_dialog_title import get_dialog_title

def test_remove_from_cart_from_home_page(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.add_to_cart("Sample Shirt Name")
  browser.implicitly_wait(2)

  home_page.remove_from_cart("Sample Shirt Name")
  assert get_notification(browser) == "Removed from cart"

def test_remove_from_cart_from_cart_page_via_remove_button(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)

  home_page.add_to_cart("Sample Shirt Name")
  assert get_notification(browser) == "Added to cart"

  home_page.click_cart()
  cart_wrapper = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='cart']"))
  )
  assert cart_wrapper.find_element(By.XPATH, ".//h3").text == "Your Cart"
  assert "/cart" in browser.current_url

  cart_page = CartPage(browser, logger)
  cart_page.click_remove("Sample Shirt Name")
  assert get_dialog_title(browser) == "Are you absolutely sure?"

  cart_page.click_confirmation_remove()
  assert browser.find_element(By.XPATH, "//h1").text == "Your cart is empty."

def test_remove_from_cart_from_cart_page_via_decrease_quantity_button(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.add_to_cart("Sample Shirt Name")
  assert get_notification(browser) == "Added to cart"

  home_page.click_cart()
  WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='cart']"))
  )
  assert "/cart" in browser.current_url

  cart_page = CartPage(browser, logger)
  assert cart_page.get_quantity("Sample Shirt Name") == 1

  cart_page.click_decrease_quantity("Sample Shirt Name")
  assert get_dialog_title(browser) == "Are you absolutely sure?"

  cart_page.click_confirmation_remove()
  assert browser.find_element(By.XPATH, "//h1").text == "Your cart is empty."
