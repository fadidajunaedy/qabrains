from utils.ecommerce.login import login
from pages.ecommerce.home_page import HomePage
from pages.ecommerce.detail_product_page import DetailProductPage
from pages.ecommerce.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart_from_home_page(browser, logger):
  login(browser, logger)
  page = HomePage(browser, logger)
  page.add_product_to_cart("Sample Shirt Name")

  notifications_section = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@aria-label, 'Notifications')]"))
  )
  notification_message = notifications_section.find_element(By.XPATH, ".//ol/li/div/div")
  assert notification_message.text == "Added to cart"

def test_remove_from_cart_from_home_page(browser, logger):
  login(browser, logger)
  page = HomePage(browser, logger)
  page.add_product_to_cart("Sample Shirt Name")

  browser.implicitly_wait(2)
  page.remove_product_from_cart("Sample Shirt Name")

  notifications_section = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@aria-label, 'Notifications')]"))
  )
  notification_message = notifications_section.find_element(By.XPATH, ".//ol/li/div/div")
  assert notification_message.text == "Removed from cart"

def test_add_to_cart_from_detail_product_page(browser, logger):
  login(browser, logger)
  page = HomePage(browser, logger)
  page.click_product("Sample Shirt Name")

  detail_wrapper = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='product-details-wrapper']"))
  )
  assert detail_wrapper.find_element(By.XPATH, ".//h1").text == "Sample Shirt Name"
  assert "/product-details" in browser.current_url

  detail_product_page = DetailProductPage(browser, logger)
  detail_product_page.increase_quantity_product()
  detail_product_page.decrease_quantity_product()
  detail_product_page.add_product_to_cart()

  notifications_section = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@aria-label, 'Notifications')]"))
  )
  notification_message = notifications_section.find_element(By.XPATH, ".//ol/li/div/div")
  assert notification_message.text == "Added to cart"

def test_increase_and_decreasing_quantity_from_cart_page(browser, logger):
  login(browser, logger)
  page = HomePage(browser, logger)
  page.add_product_to_cart("Sample Shirt Name")

  notifications_section = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@aria-label, 'Notifications')]"))
  )
  notification_message = notifications_section.find_element(By.XPATH, ".//ol/li/div/div")
  assert notification_message.text == "Added to cart"

  page.click_cart_link_button()
  cart_page = CartPage(browser, logger)
  cart_page.click_increase_quantity("Sample Shirt Name")
  assert int(cart_page.get_quantity("Sample Shirt Name")) == 2
  cart_page.click_decrease_quantity("Sample Shirt Name")
  assert int(cart_page.get_quantity("Sample Shirt Name")) == 1

def test_remove_from_cart_from_cart_page_via_remove_button(browser, logger):
  login(browser, logger)
  page = HomePage(browser, logger)
  page.add_product_to_cart("Sample Shirt Name")

  notifications_section = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@aria-label, 'Notifications')]"))
  )
  notification_message = notifications_section.find_element(By.XPATH, ".//ol/li/div/div")
  assert notification_message.text == "Added to cart"

  page.click_cart_link_button()
  cart_page = CartPage(browser, logger)
  cart_page.click_remove("Sample Shirt Name")

  dialog_overlay = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, "//div[@data-slot='dialog-overlay' and @data-state='open']"))
  )

  dialog = dialog_overlay.find_element(By.XPATH, "./following-sibling::div[@role='dialog']")
  dialog_title = dialog.find_element(By.XPATH, ".//h2")
  assert dialog_title.text == "Are you absolutely sure?"

  cart_page.click_confirmation_remove()


