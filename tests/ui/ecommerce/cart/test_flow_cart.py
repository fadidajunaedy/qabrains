from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage
from pages.ecommerce.detail_page import DetailPage
from pages.ecommerce.cart_page import CartPage

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification

def test_flow_cart(browser, logger):
  logger.info("=== [START] TEST FLOW CART ===")
  try:
    login(browser, logger)
    home_page = HomePage(browser, logger)

    # adding cart from home page
    home_page.add_to_cart("Sample Shirt Name")
    assert get_notification(browser) == "Added to cart"

    # through detail page
    home_page.click_product("Sample Shoe Name")
    detail_wrapper = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[@class='product-details-wrapper']"))
    )
    assert detail_wrapper.find_element(By.XPATH, ".//h1").text == "Sample Shoe Name"
    assert "/product-details" in browser.current_url

    # adding quantity from default 1 to 2
    detail_page = DetailPage(browser, logger)
    assert detail_page.get_quantity() == 1
    detail_page.increase_quantity()
    assert detail_page.get_quantity() == 2

    # adding cart from detail page
    detail_page.add_to_cart()

    # go to cart page
    home_page.click_cart()
    WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[@id='cart']"))
    )
    assert "/cart" in browser.current_url

    cart = WebDriverWait(browser, 5).until(
      EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'cart-list')]//h3"))
    )
    texts = [product.text for product in cart]
    # making sure product that add from home page is added
    assert "Sample Shirt Name" in texts, f"Cart list: {texts}"
    # making sure product that add from detail page is added
    assert "Sample Shoe Name" in texts, f"Cart list: {texts}"

    cart_page = CartPage(browser, logger)
    cart_page.click_increase_quantity("Sample Shirt Name") # increasing quantity from cart page
    quantity_product_shirt = cart_page.get_quantity("Sample Shirt Name")
    price_product_shirt = cart_page.get_price("Sample Shirt Name")
    total_product_shirt = cart_page.get_total("Sample Shirt Name")

    assert quantity_product_shirt == 2
    assert total_product_shirt == price_product_shirt * quantity_product_shirt

    cart_page.click_decrease_quantity("Sample Shoe Name") # decreasing quantity from cart page
    quantity_product_shoe = cart_page.get_quantity("Sample Shoe Name")
    price_product_shoe = cart_page.get_price("Sample Shoe Name")
    total_product_shoe = cart_page.get_total("Sample Shoe Name")

    assert quantity_product_shoe == 1
    assert total_product_shoe == price_product_shoe * quantity_product_shoe
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST FLOW CART ===")
