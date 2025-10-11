from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage
from pages.ecommerce.detail_page import DetailPage

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification

def test_add_favorite_from_home_page(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.toggling_favorite("Sample Shirt Name")
  assert get_notification(browser) == "Added to favorites"

def test_add_favorite_from_detail_page(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.click_product("Sample Shirt Name")

  detail_wrapper = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='product-details-wrapper']"))
  )
  assert detail_wrapper.find_element(By.XPATH, ".//h1").text == "Sample Shirt Name"
  assert "/product-details" in browser.current_url

  detail_page = DetailPage(browser, logger)
  detail_page.toggling_favorite()
  assert get_notification(browser) == "Added to favorites"
