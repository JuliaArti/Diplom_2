import allure
from data import RegisterUser
from helpers import Helpers

class TestUserRegistration:
    @allure.title('Проверка регимстрация пользователя')
    @allure.description('Регистрируем пользователя с полными данными')
    def test_register_user_success(self, generate_user_data):
        # Arrange
        api = generate_user_data[0]
        login = generate_user_data[1]["email"]
        password = generate_user_data[1]["password"]
        name = generate_user_data[1]["name"]

        # Act
        response = api.create_user(login, password, name)
        
        # Assert
        # Проверяем код ответа
        assert response.status_code == RegisterUser.register_res_ok_code, f"Ожидали код {RegisterUser.register_res_ok_code}, получили {response.status_code}"
        
        # Проверяем контент ответа
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, RegisterUser.register_res_body_ok), f"Ожидали тело {RegisterUser.register_res_body_ok}, получили {response_data}"
    
    @allure.title('Проверка регимстрация пользователя, который уже существует')
    @allure.description('Регистрируем пользователя дважды')
    def test_register_duplicate_user(self, generate_user_data):
        # Arrange
        api = generate_user_data[0]
        login = generate_user_data[1]["email"]
        password = generate_user_data[1]["password"]
        name = generate_user_data[1]["name"]

        # Act
        api.create_user(login, password, name)
        response2 = api.create_user(login, password, name)
        
        # Assert
        # Проверяем код ответа
        assert response2.status_code == RegisterUser.register_res_code_already_exists, f"Ожидали код {RegisterUser.register_res_code_already_exists}, получили {response2.status_code}"
        
        # Проверяем контент ответа
        response_data = response2.json()
        assert Helpers.check_json_contains_template(response_data, RegisterUser.register_res_body_already_exists), f"Ожидали тело {RegisterUser.register_res_body_already_exists}, получили {response_data}"

    @allure.title('Проверка регимстрация пользователя без необходимых данных')
    @allure.description('Регистрируем пользователя без имени')
    def test_register_user_no_data(self, generate_user_data):
        # Arrange
        api = generate_user_data[0]
        login = generate_user_data[1]["email"]
        password = generate_user_data[1]["password"]

        # Act
        response = api.create_user(login, password)
       
        # Assert
        # Проверяем код ответа
        assert response.status_code == RegisterUser.register_res_code_no_data, f"Ожидали код {RegisterUser.register_res_code_no_data}, получили {response.status_code}"
        
        # Проверяем контент ответа
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, RegisterUser.register_res_body_no_data), f"Ожидали тело {RegisterUser.register_res_body_no_data}, получили {response_data}"