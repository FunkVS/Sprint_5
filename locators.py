from selenium.webdriver.common.by import By

class MainPage:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    AD_ERROR_TEXT = (By.XPATH, "//h1[contains(@class, 'h1') and contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    AD_ERROR_WINDOW = (By.XPATH, "//form[contains(@class, 'popUp_shell__LuyqR')]")
    USER_AVATAR = (By.XPATH, "//button[@class='circleSmall']")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[@class='arrowButton arrowButton--right undefined']")

class AuthPage:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    EMAIL_ERROR = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(text(), 'Логин или пароль неверны')]")

class ProfilePage:
    MY_ADS_SECTION = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
    AD_TITLE_AND_CITY = (By.XPATH, "//div[@class='description']")
    AD_PRICE = (By.XPATH, "//div[@class='price']")

class AdPage:
    AD_NAME = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal']")
    AD_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    AD_PRICE = (By.NAME, "price")
    DROPDOWN_CATEGORY = (By.CSS_SELECTOR, "input[name='category'] + button")
    DROPDOWN_CHOOSE_CATEGORY = (By.XPATH, "//span[contains(text(), 'Технологии')]")
    DROPDOWN_CITY = (By.CSS_SELECTOR, "input[name='city'] + button")
    DROPDOWN_CHOOSE_CITY = (By.XPATH, "//span[contains(text(), 'Екатеринбург')]")
    AD_RADIOBUTTON = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")
    AD_CREATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")