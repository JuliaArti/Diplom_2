import requests
import allure
from urls import Url

class BurgersAPI:
    @allure.step('Создаем пользователя')
    def create_user(self, email=None, password=None, name=None):
        url = Url.BASE_URL + Url.CREATE_USER
        payload = {}
        
        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password
        if name is not None:
            payload["name"] = name

        response = requests.post(url, json=payload)
        return response
    @allure.step('Авторизация с использованием логина и пароля')
    def auth_user(self, email=None, password=None):
        url = Url.BASE_URL + Url.AUTH_USER
        payload = {}
        
        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password

        response = requests.post(url, json=payload)
        return response
    
    @allure.step('Удаление пользователя')
    def delete_user(self, acccess_token=None):
        url = Url.BASE_URL + Url.DELETE_USER
        headers = {}

        if acccess_token is not None:
            headers["Authorization"] = acccess_token

        response = requests.delete(url, headers=headers)
        return response
    
    @allure.step('Создание заказа')
    def create_order(self, acccess_token=None, ingredients=None):
        url = Url.BASE_URL + Url.ORDERS_ENDPOINT
        headers = {}
        payload = {}

        if acccess_token is not None:
            headers["Authorization"] = acccess_token
        if ingredients is not None:
            payload["ingredients"] = ingredients

        response = requests.post(url, json=payload, headers=headers)
        return response
    
    @allure.step('Получение списка ингридиентов')
    def get_ingredients_list(self):
        url = Url.BASE_URL + Url.IMGREDIENTS_ENDPOINT

        response = requests.get(url)
        return response