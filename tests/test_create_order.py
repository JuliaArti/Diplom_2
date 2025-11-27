import allure
import pytest
from data import CreateOrder
from helpers import Helpers

class TestUserAuthentication:
    @pytest.mark.parametrize(
        "ingredients_count, expected_status, expected_template, test_description",
        CreateOrder.test_order_success_with_auth_cases
    )
    @allure.title('Проверка успешного заказа {test_description}')
    @allure.description('Делаем заказ {test_description}')
    def test_order_success_with_auth(self, create_authenticated_user, ingredients_count, 
                                   expected_status, expected_template, test_description):
        # Arrange
        api = create_authenticated_user[0]
        access_token = create_authenticated_user[1]["access_token"]
        
        # Act
        ingredients_response = api.get_ingredients_list()
        ingredients = ingredients_response.json()
        ingredients_list = [ingredients["data"][i]["_id"] for i in range(ingredients_count)]
        response = api.create_order(access_token, ingredients_list)

        # Assert
        assert response.status_code == expected_status, f"Ожидали код {expected_status}, получили {response.status_code}"
        
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, expected_template), f"Ожидали тело {expected_template}, получили {response_data}"

    @pytest.mark.parametrize(
        "ingredients_list, expected_status, expected_template, test_description", 
        CreateOrder.test_order_with_incorrect_ingredients_cases
        )      
    
    @allure.title('Проверка заказа {test_description}')
    @allure.description('При создании заказа {test_description}')
    def test_order_with_incorrect_ingredients(self, create_authenticated_user, ingredients_list,
                                         expected_status, expected_template, test_description):
        # Arrange
        api = create_authenticated_user[0]
        access_token = create_authenticated_user[1]["access_token"]
        
        # Act
        response = api.create_order(access_token, ingredients_list)

        # Assert
        assert response.status_code == expected_status, f"Ожидали код {expected_status}, получили {response.status_code}"
        
        if not expected_template is None:
            response_data = response.json()
            assert Helpers.check_json_contains_template(response_data, expected_template), f"Ожидали тело {expected_template}, получили {response_data}"

    @allure.title('Проверка заказа без авторизации')
    @allure.description('При создании заказа не передаем заголовок Authorization')
    def test_order_no_auth(self, generate_user_data):
        # Arrange
        api = generate_user_data[0]
        
        # Act
        ingredients_response = api.get_ingredients_list()
        ingredients = ingredients_response.json()
        ingredients_list = [ingredients["data"][0]["_id"], ingredients["data"][1]["_id"], 
                          ingredients["data"][2]["_id"]]
        response = api.create_order(ingredients=ingredients_list)

        # Assert
        assert response.status_code == CreateOrder.order_res_no_auth_code, f"Ожидали код {CreateOrder.order_res_no_auth_code}, получили {response.status_code}"
        
        response_data = response.json()
        assert Helpers.check_json_contains_template(response_data, CreateOrder.order_res_body_no_auth), f"Ожидали тело {CreateOrder.order_res_body_no_auth}, получили {response_data}"