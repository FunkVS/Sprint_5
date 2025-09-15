import pytest

from data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPage, MainPage, AdPage, ProfilePage

class TestCreateAd:
    """Тесты создания объявлений"""
    
    def test_create_ad_unauthorized(self, driver):
        """Создание объявления неавторизованным пользователем"""
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(MainPage.CREATE_AD_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(MainPage.AD_ERROR_WINDOW))
        
        assert wait.until(EC.visibility_of_element_located(MainPage.AD_ERROR_TEXT))

    def test_create_ad_authorized(self, driver):
        """Создание объявления авторизованным пользователем"""
        
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPage.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(AuthPage.EMAIL_INPUT)).send_keys(TestData.unique_email())
        wait.until(EC.visibility_of_element_located(AuthPage.PASSWORD_INPUT)).send_keys("Password123!")
        wait.until(EC.visibility_of_element_located(AuthPage.CONFIRM_PASSWORD_INPUT)).send_keys("Password123!")

        wait.until(EC.element_to_be_clickable(AuthPage.CREATE_ACCOUNT_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(MainPage.USER_AVATAR))
        wait.until(EC.visibility_of_element_located(MainPage.USER_NAME))
        
        wait.until(EC.element_to_be_clickable(MainPage.CREATE_AD_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(AdPage.AD_NAME)).send_keys(TestData.unique_ad_title())
        wait.until(EC.visibility_of_element_located(AdPage.AD_DESCRIPTION)).send_keys("Описание товара")
        wait.until(EC.visibility_of_element_located(AdPage.AD_PRICE)).send_keys("1000")

        wait.until(EC.visibility_of_element_located(AdPage.DROPDOWN_CATEGORY)).click()
        wait.until(EC.visibility_of_element_located(AdPage.DROPDOWN_CHOOSE_CATEGORY)).click()

        wait.until(EC.visibility_of_element_located(AdPage.DROPDOWN_CITY)).click()
        wait.until(EC.visibility_of_element_located(AdPage.DROPDOWN_CHOOSE_CITY)).click()

        wait.until(EC.visibility_of_element_located(AdPage.AD_RADIOBUTTON)).click()

        wait.until(EC.visibility_of_element_located(AdPage.AD_CREATE_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(MainPage.NEXT_PAGE_BUTTON))
        wait.until(EC.visibility_of_element_located(MainPage.USER_AVATAR)).click()
        ad_title_and_city = wait.until(EC.visibility_of_element_located(ProfilePage.AD_TITLE_AND_CITY))
        ad_price = wait.until(EC.visibility_of_element_located(ProfilePage.AD_PRICE))

        assert ad_title_and_city and ad_price
