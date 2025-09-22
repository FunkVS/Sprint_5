import pytest

from data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPage, MainPage


class TestRegistration:
    """Тесты регистрации пользователя"""
    
    def test_successful_registration(self, driver):
        """Регистрация пользователя"""
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPage.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(AuthPage.EMAIL_INPUT)).send_keys(TestData.unique_email())
        wait.until(EC.visibility_of_element_located(AuthPage.PASSWORD_INPUT)).send_keys("Password123!")
        wait.until(EC.visibility_of_element_located(AuthPage.CONFIRM_PASSWORD_INPUT)).send_keys("Password123!")

        wait.until(EC.element_to_be_clickable(AuthPage.CREATE_ACCOUNT_BUTTON)).click()

        assert wait.until(EC.invisibility_of_element_located(MainPage.LOGIN_BUTTON))


    def test_registration_invalid_email(self, driver):
        """Регистрация с невалидным email"""
        wait = WebDriverWait(driver, 5)


        wait.until(EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPage.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(AuthPage.EMAIL_INPUT)).send_keys("invalid-email")
        wait.until(EC.visibility_of_element_located(AuthPage.PASSWORD_INPUT)).send_keys("Password123!")
        wait.until(EC.visibility_of_element_located(AuthPage.CONFIRM_PASSWORD_INPUT)).send_keys("Password123!")

        wait.until(EC.element_to_be_clickable(AuthPage.CREATE_ACCOUNT_BUTTON)).click()

        assert wait.until(EC.visibility_of_element_located(AuthPage.EMAIL_ERROR))

    def test_registration_existing_user(self, driver):
        """Регистрация существующего пользователя"""
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPage.NO_ACCOUNT_BUTTON)).click()


        wait.until(EC.visibility_of_element_located(AuthPage.EMAIL_INPUT)).send_keys(TestData.existing_user()["email"])
        wait.until(EC.visibility_of_element_located(AuthPage.PASSWORD_INPUT)).send_keys("Password123!")
        wait.until(EC.visibility_of_element_located(AuthPage.CONFIRM_PASSWORD_INPUT)).send_keys("Password123!")

        wait.until(EC.element_to_be_clickable(AuthPage.CREATE_ACCOUNT_BUTTON)).click()
        
        assert wait.until(EC.visibility_of_element_located(AuthPage.EMAIL_ERROR))
