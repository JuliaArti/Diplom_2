import allure
from data import CreateOrder
from helpers import Helpers

class TestUserAuthentication:
    @allure.title('Проверка успешного заказа с авторизацией')
    @allure.description('Делаем заказ с 1 ингредиентом и авторизацией')
    def test_order_success(self, create_authenticated_user):
        # Arrange
        api = create_authenticated_user[0]
        access_token = create_authenticated_user[1]["access_token"]
        
        # Act
        ingredients_response = api.get_ingredients_list()
        ingredients = ingredients_response.json()
        ingredients_list = [ingredients["data"][0]["_id"]]
        response = api.create_order(access_token, ingredients_list)

        # Assert
        # Проверяем код ответа
        assert response.status_code == CreateOrder.order_res_ok_code, f"Ожидали код {CreateOrder.order_res_ok_code}, получили {response.status_code}"
        
        # Проверяем контент ответа
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, CreateOrder.order_res_body_ok), f"Ожидали тело {CreateOrder.order_res_body_ok}, получили {response_data}"

    @allure.title('Проверка заказа без авторизации')
    @allure.description('При создании заказа не передаем заголовок Authorization')
    def test_order_no_auth(self, generate_user_data):
        # Arrange
        api = generate_user_data[0]
        
        # Act
        ingredients_response = api.get_ingredients_list()
        ingredients = ingredients_response.json()
        ingredients_list = [ingredients["data"][0]["_id"], ingredients["data"][1]["_id"], ingredients["data"][2]["_id"]]
        response = api.create_order(ingredients = ingredients_list)

        # Assert
        # Проверяем код ответа
        assert response.status_code == CreateOrder.order_res_no_auth_code, f"Ожидали код {CreateOrder.order_res_no_auth_code}, получили {response.status_code}"
        
        # Проверяем контент ответа
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, CreateOrder.order_res_body_no_auth), f"Ожидали тело {CreateOrder.order_res_body_no_auth}, получили {response_data}"

    @allure.title('Проверка заказа с несколькими ингредиентами')
    @allure.description('Делаем заказ с 3 ингредиентами')
    def test_order_mult_ingredients(self, create_authenticated_user):
        # Arrange
        api = create_authenticated_user[0]
        access_token = create_authenticated_user[1]["access_token"]
        
        # Act
        ingredients_response = api.get_ingredients_list()
        ingredients = ingredients_response.json()
        ingredients_list = [ingredients["data"][0]["_id"], ingredients["data"][1]["_id"], ingredients["data"][2]["_id"]]
        response = api.create_order(access_token, ingredients_list)

        # Assert
        # Проверяем код ответа
        assert response.status_code == CreateOrder.order_res_ok_code, f"Ожидали код {CreateOrder.order_res_ok_code}, получили {response.status_code}"
        
        # Проверяем контент ответа
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, CreateOrder.order_res_body_ok), f"Ожидали тело {CreateOrder.order_res_body_ok}, получили {response_data}"

    @allure.title('Проверка заказа без ингредиентов')
    @allure.description('При создании заказа передаем пустой список ингредиентов')
    def test_order_no_ingredients(self, create_authenticated_user):
        # Arrange
        api = create_authenticated_user[0]
        access_token = create_authenticated_user[1]["access_token"]
        
        # Act
        ingredients_list = []
        response = api.create_order(access_token, ingredients_list)

        # Assert
        # Проверяем код ответа
        assert response.status_code == CreateOrder.order_res_no_ingredients_code, f"Ожидали код {CreateOrder.order_res_no_ingredients_code}, получили {response.status_code}"
        
        # Проверяем контент ответа
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, CreateOrder.order_res_body_no_ingredients), f"Ожидали тело {CreateOrder.order_res_body_no_ingredients}, получили {response_data}"

    @allure.title('Проверка заказа с неверным хешом ингредиента')
    @allure.description('При создании заказа передаем неверный хеш ингредиента')
    def test_order_wong_hash(self, create_authenticated_user):
        # Arrange
        api = create_authenticated_user[0]
        access_token = create_authenticated_user[1]["access_token"]
        
        # Act
        ingredients_list = ["123wronghash53453"]
        response = api.create_order(access_token, ingredients_list)

        # Assert
        # Проверяем код ответа
        assert response.status_code == CreateOrder.order_res_wrong_ingredients_hash_code, f"Ожидали код {CreateOrder.order_res_wrong_ingredients_hash_code}, получили {response.status_code}"
