from utils.ecommerce.login import login
from pages.ecommerce.home_page import HomePage
from pages.ecommerce.detail_page import DetailPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_favorite_from_home_page(browser, logger):
  login(browser, logger)
  page = HomePage(browser, logger)
  page.toggling_favorite("Sample Shirt Name")
  notifications_section = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@aria-label, 'Notifications')]"))
  )
  notification_message = notifications_section.find_element(By.XPATH, ".//ol/li/div/div")
  assert notification_message.text == "Added to favorites"

def test_add_favorite_from_detail_page(browser, logger):
  login(browser, logger)
  page = HomePage(browser, logger)
  page.click_product("Sample Shirt Name")

  detail_wrapper = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='product-details-wrapper']"))
  )
  assert detail_wrapper.find_element(By.XPATH, ".//h1").text == "Sample Shirt Name"
  assert "/product-details" in browser.current_url

  detail_page = DetailPage(browser, logger)
  detail_page.toggling_favorite()

  notifications_section = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@aria-label, 'Notifications')]"))
  )
  notification_message = notifications_section.find_element(By.XPATH, ".//ol/li/div/div")
  assert notification_message.text == "Added to favorites"
