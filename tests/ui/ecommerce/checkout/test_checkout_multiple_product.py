from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage
from pages.ecommerce.cart_page import CartPage
from pages.ecommerce.checkout_info_page import CheckoutInfoPage
from pages.ecommerce.checkout_overview_page import CheckoutOverviewPage

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification

def test_checkout_multiple_product_one_quantity(browser, logger):
  logger.info("=== [START] TEST CHECKOUT MULTIPLE PRODUCT ONE QUANTITY ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.add_to_cart("Sample Shirt Name")
    home_page.add_to_cart("Sample Shoe Name")
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
    assert "Sample Shoe Name" in texts, f"Cart list: {texts}"

    cart_page = CartPage(browser, logger)
    cart_page.click_checkout_button()

    checkout_info_page = CheckoutInfoPage(browser, logger)
    checkout_info_page.enter_first_name("Fadida")
    checkout_info_page.enter_last_name("Junaedy")
    checkout_info_page.click_continue_button()

    checkout_overview_page = CheckoutOverviewPage(browser, logger)
    quantity_per_product_1 = checkout_overview_page.get_quantity_per_product("Sample Shirt Name")
    price_per_product_1 = checkout_overview_page.get_price_per_product("Sample Shirt Name")
    total_per_product_1 = checkout_overview_page.get_total_per_product("Sample Shirt Name")
    assert quantity_per_product_1 == 1
    assert total_per_product_1 == price_per_product_1 * quantity_per_product_1

    quantity_per_product_2 = checkout_overview_page.get_quantity_per_product("Sample Shoe Name")
    price_per_product_2 = checkout_overview_page.get_price_per_product("Sample Shoe Name")
    total_per_product_2 = checkout_overview_page.get_total_per_product("Sample Shoe Name")
    assert quantity_per_product_2 == 1
    assert total_per_product_2 == price_per_product_2 * quantity_per_product_2

    total = checkout_overview_page.get_total()
    tax = checkout_overview_page.get_tax()
    total_after_tax = checkout_overview_page.get_total_after_tax()
    assert total + tax == total_after_tax

    checkout_overview_page.click_finish_button()
    checkout_complete = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[@id='checkout-complete']"))
    )
    assert "/checkout-complete" in browser.current_url
    assert browser.find_element(By.XPATH, "//h3[text() = 'Thank you for your order!']")
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST CHECKOUT MULTIPLE PRODUCT ONE QUANTITY ===")

def test_checkout_multiple_product_multiple_quantity(browser, logger):
  logger.info("=== [START] TEST CHECKOUT ONE PRODUCT MULTIPLE QUANTITY ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)
    home_page.add_to_cart("Sample Shirt Name")
    home_page.add_to_cart("Sample Shoe Name")
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
    assert "Sample Shoe Name" in texts, f"Cart list: {texts}"

    cart_page = CartPage(browser, logger)
    cart_page.click_increase_quantity("Sample Shirt Name")
    cart_page.click_increase_quantity("Sample Shoe Name")
    cart_page.click_checkout_button()

    checkout_info_page = CheckoutInfoPage(browser, logger)
    checkout_info_page.enter_first_name("Fadida")
    checkout_info_page.enter_last_name("Junaedy")
    checkout_info_page.click_continue_button()

    checkout_overview_page = CheckoutOverviewPage(browser, logger)
    quantity_per_product_1 = checkout_overview_page.get_quantity_per_product("Sample Shirt Name")
    price_per_product_1 = checkout_overview_page.get_price_per_product("Sample Shirt Name")
    total_per_product_1 = checkout_overview_page.get_total_per_product("Sample Shirt Name")
    assert quantity_per_product_1 == 2
    assert total_per_product_1 == price_per_product_1 * quantity_per_product_1

    quantity_per_product_2 = checkout_overview_page.get_quantity_per_product("Sample Shoe Name")
    price_per_product_2 = checkout_overview_page.get_price_per_product("Sample Shoe Name")
    total_per_product_2 = checkout_overview_page.get_total_per_product("Sample Shoe Name")
    assert quantity_per_product_2 == 2
    assert total_per_product_2 == price_per_product_2 * quantity_per_product_2

    total = checkout_overview_page.get_total()
    tax = checkout_overview_page.get_tax()
    total_after_tax = checkout_overview_page.get_total_after_tax()
    assert total + tax == total_after_tax

    checkout_overview_page.click_finish_button()
    checkout_complete = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[@id='checkout-complete']"))
    )
    assert "/checkout-complete" in browser.current_url
    assert browser.find_element(By.XPATH, "//h3[text() = 'Thank you for your order!']")
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST CHECKOUT ONE PRODUCT MULTIPLE QUANTITY ===")
