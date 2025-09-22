import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.logger import get_logger

@pytest.fixture
def browser():
  # setup (before test)
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service)
  driver.maximize_window()
  driver.implicitly_wait(5)
  yield driver

  # teardown (after test)
  driver.quit()

@pytest.fixture(scope="session")
def logger():
  return get_logger()
