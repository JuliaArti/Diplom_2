import allure
from data import AuthUser
from helpers import Helpers

class TestUserAuthentication:
    @allure.title('Проверка успешной авторизации пользователя')
    @allure.description('Авторизация с корректными данными')
    def test_auth_user_success(self, create_registred_user):
        # Arrange
        api = create_registred_user[0]
        login = create_registred_user[1]["email"]
        password = create_registred_user[1]["password"]

        # Act
        response = api.auth_user(login, password)

        # Assert
        # Проверяем код ответа
        assert response.status_code == AuthUser.auth_res_ok_code, f"Ожидали код {AuthUser.auth_res_ok_code}, получили {response.status_code}"
        
        # Проверяем контент ответа
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, AuthUser.auth_res_body_ok), f"Ожидали тело {AuthUser.auth_res_body_ok}, получили {response_data}"

    @allure.title('Проверка авторизации пользователя с ошибкой')
    @allure.description('Авторизация с неправильным паролем')
    def test_auth_user_failed(self, create_registred_user):
        # Arrange
        api = create_registred_user[0]
        login = create_registred_user[1]["email"]

        # Act
        response = api.auth_user(login, "wrong_pass")

        # Assert
        # Проверяем код ответа
        assert response.status_code == AuthUser.auth_res_code_wrong_data, f"Ожидали {AuthUser.auth_res_code_wrong_data}, получили {response.status_code}"
        
        # Проверяем контент ответа
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, AuthUser.auth_res_body_wrong_data), f"Ожидали тело {AuthUser.auth_res_body_wrong_data}, получили {response_data}"