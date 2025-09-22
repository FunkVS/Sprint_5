import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(
        options=chrome_options
    )
    driver.maximize_window()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    yield driver
    driver.quit()
