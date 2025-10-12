from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ecommerce.home_page import HomePage
from pages.ecommerce.favorites_page import FavoritesPage

from utils.ecommerce.login import login
from utils.ecommerce.get_notification import get_notification

def test_favorite_flow(browser, logger):
  logger.info("=== [START] TEST FAVORITE FLOW ===")
  try:
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

    favorites_page = FavoritesPage(browser, logger)
    favorites_page.toggling_favorite("Sample Shirt Name")
    assert get_notification(browser) == "Removed from favorites"

    assert browser.find_element(By.XPATH, "//div[@id='favorites-wrapper']//h2").text == "You have no favorite products"
  except Exception as e:
    logger.error(f"Test failed due to: {e}")
    raise
  finally:
    logger.info("=== [END] TEST FAVORITE FLOW ===")
