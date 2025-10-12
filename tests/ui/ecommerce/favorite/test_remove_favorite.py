from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification
from pages.ecommerce.home_page import HomePage
from pages.ecommerce.detail_page import DetailPage
from pages.ecommerce.favorites_page import FavoritesPage

def test_remove_favorite_from_home_page(browser, logger):
  logger.info("=== [START] TEST REMOVE FAVORITE FROM HOME PAGE ===")
  try:
    login(browser, logger)
    page = HomePage(browser, logger)
    page.toggling_favorite("Sample Shirt Name")
    browser.implicitly_wait(2)
    page.toggling_favorite("Sample Shirt Name")

    assert get_notification(browser) == "Removed from favorites"
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST REMOVE FAVORITE FROM HOME PAGE ===")

def test_remove_favorite_from_detail_page(browser, logger):
  logger.info("=== [START] TEST REMOVE FAVORITE FROM DETAIL PAGE ===")
  try:
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
    browser.implicitly_wait(2)
    detail_page.toggling_favorite()
    assert get_notification(browser) == "Removed from favorites"
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST REMOVE FAVORITE FROM DETAIL PAGE ===")

def test_remove_favorite_from_favorites_page(browser, logger):
  logger.info("=== [START] TEST REMOVE FAVORITE FROM FAVORITES PAGE ===")
  try:
    login(browser, logger)
    page = HomePage(browser, logger)
    page.toggling_favorite("Sample Shirt Name")
    assert get_notification(browser) == "Added to favorites"

    page.open_menu_dropdown()
    page.click_favorites()

    favorites = WebDriverWait(browser, 5).until(
      EC.presence_of_all_elements_located((By.XPATH, "//div[@id='favorites-wrapper']/div[contains(@class, 'products')]//a/following-sibling::a"))
    )
    texts = [favorite.text for favorite in favorites]
    assert "Sample Shirt Name" in texts, f"Favorites list: {texts}"

    favorites_page = FavoritesPage(browser, logger)
    favorites_page.toggling_favorite("Sample Shirt Name")
    assert get_notification(browser) == "Removed from favorites"
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST REMOVE FAVORITE FROM FAVORITES PAGE ===")





