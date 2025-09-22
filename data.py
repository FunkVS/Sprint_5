import random
import string


class TestData:
    @staticmethod
    def existing_user():
        """Данные существующего пользователя"""
        return {
            "email": "practicumfunk@mail.ru",
            "password": "TestPassword123!"
        }
    
    @staticmethod
    def unique_email():
        """Генерация уникального email"""
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{username}@example.com"
    
    @staticmethod
    def unique_ad_title():
        """Генерация уникального названия объявления"""
        prefix = ''.join(random.choices(string.ascii_lowercase, k=6))
        return f"Test Ad {prefix}"