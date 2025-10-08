from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage
from pages.ecommerce.detail_page import DetailPage
from pages.ecommerce.cart_page import CartPage

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification
from utils.ecommerce.get_dialog_title import get_dialog_title

def test_increase_quantity_cart_from_detail_page(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.click_product("Sample Shirt Name")

  detail_wrapper = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='product-details-wrapper']"))
  )
  assert detail_wrapper.find_element(By.XPATH, ".//h1").text == "Sample Shirt Name"
  assert "/product-details" in browser.current_url

  detail_page = DetailPage(browser, logger)
  assert detail_page.get_quantity() == 1

  detail_page.increase_quantity()
  assert detail_page.get_quantity() == 2

def test_decrease_quantity_cart_from_detail_page(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.click_product("Sample Shirt Name")

  detail_wrapper = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='product-details-wrapper']"))
  )
  assert detail_wrapper.find_element(By.XPATH, ".//h1").text == "Sample Shirt Name"
  assert "/product-details" in browser.current_url

  detail_page = DetailPage(browser, logger)
  detail_page.increase_quantity()
  assert detail_page.get_quantity() == 2
  detail_page.decrease_quantity()
  assert detail_page.get_quantity() == 1

def test_increase_quantity_cart_from_cart_page(browser, logger):
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
  cart_page.click_increase_quantity("Sample Shirt Name")

  quantity = cart_page.get_quantity("Sample Shirt Name")
  price = cart_page.get_price("Sample Shirt Name")
  total = cart_page.get_total("Sample Shirt Name")

  assert quantity == 2
  assert total == price * quantity

def test_decrease_quantity_cart_from_cart_page(browser, logger):
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
  cart_page.click_increase_quantity("Sample Shirt Name")
  quantity = cart_page.get_quantity("Sample Shirt Name")
  price = cart_page.get_price("Sample Shirt Name")
  total = cart_page.get_total("Sample Shirt Name")

  assert quantity == 2
  assert total == price * quantity

  cart_page.click_decrease_quantity("Sample Shirt Name")
  quantity = cart_page.get_quantity("Sample Shirt Name")
  price = cart_page.get_price("Sample Shirt Name")
  total = cart_page.get_total("Sample Shirt Name")

  assert quantity == 1
  assert total == price * quantity
