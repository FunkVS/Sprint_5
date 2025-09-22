import pytest

from data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPage, MainPage


def test_successful_login(driver):
    """Авторизация пользователя"""
    
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)).click()
    
    wait.until(EC.visibility_of_element_located(AuthPage.EMAIL_INPUT)).send_keys(TestData.existing_user()["email"])
    wait.until(EC.visibility_of_element_located(AuthPage.PASSWORD_INPUT)).send_keys(TestData.existing_user()["password"])
    wait.until(EC.element_to_be_clickable(AuthPage.LOGIN_BUTTON)).click()
    
    user_avatar = wait.until(EC.visibility_of_element_located(MainPage.USER_AVATAR))
    user_name = wait.until(EC.visibility_of_element_located(MainPage.USER_NAME))

    assert user_avatar and user_name
