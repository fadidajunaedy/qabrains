from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification

def test_favorites_page_empty_state(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.open_menu_dropdown()
  home_page.click_favorites()

  WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='favorites-wrapper']"))
  )
  assert browser.find_element(By.XPATH, "//div[@id='favorites-wrapper']//h2").text == "You have no favorite products"

def test_favorites_page_shows_added(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.toggling_favorite("Sample Shirt Name")
  assert get_notification(browser) == "Added to favorites"

  home_page.open_menu_dropdown()
  home_page.click_favorites()

  favorites = WebDriverWait(browser, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@id='favorites-wrapper']/div[contains(@class, 'products')]//a/following-sibling::a"))
  )
  texts = [favorite.text for favorite in favorites]
  assert "Sample Shirt Name" in texts, f"Favorites list: {texts}"

def test_favorites_page_shows_added_after_refresh(browser, logger):
  login(browser, logger)
  home_page = HomePage(browser, logger)
  home_page.toggling_favorite("Sample Shirt Name")
  assert get_notification(browser) == "Added to favorites"

  home_page.open_menu_dropdown()
  home_page.click_favorites()

  favorites = WebDriverWait(browser, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@id='favorites-wrapper']/div[contains(@class, 'products')]//a/following-sibling::a"))
  )
  texts = [favorite.text for favorite in favorites]
  assert "Sample Shirt Name" in texts, f"Favorites list: {texts}"

  browser.refresh()

  favorites = WebDriverWait(browser, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@id='favorites-wrapper']/div[contains(@class, 'products')]//a/following-sibling::a"))
  )
  texts = [favorite.text for favorite in favorites]
  assert "Sample Shirt Name" in texts, f"Favorites list: {texts}"
