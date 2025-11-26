class RegisterUser:
    register_res_ok_code = 200
    register_res_body_ok = {
        "success": True
    }
    
    register_res_code_no_data = 403
    register_res_body_no_data = {
        "success":False,
        "message":"Email, password and name are required fields"
    }

    register_res_code_already_exists = 403
    register_res_body_already_exists = {
        "success": False,
        "message": "User already exists"
    }

class AuthUser:
    auth_res_ok_code = 200
    auth_res_body_ok = {
        "success": True
    }
    
    auth_res_code_wrong_data = 401
    auth_res_body_wrong_data = {
        "success":False,
        "message":"email or password are incorrect"
    }

class CreateOrder:
    order_res_ok_code = 200
    order_res_body_ok = {
        "success": True
    }

    order_res_no_ingredients_code = 400
    order_res_body_no_ingredients = {
        "success": False,
        "message":"Ingredient ids must be provided"
    }

    order_res_no_auth_code = 403
    order_res_body_no_auth = {
        "success": False
    }

    order_res_wrong_ingredients_hash_code = 500


    test_order_success_with_auth_cases = [
            (1, order_res_ok_code, order_res_body_ok, 
             "с 1 ингредиентом и авторизацией"),
            (3, order_res_ok_code, order_res_body_ok,
             "с 3 ингредиентами и авторизацией"),
    ]

    test_order_with_incorrect_ingredients_cases = [
            ([], order_res_no_ingredients_code, order_res_body_no_ingredients, "без ингредиентов"),
            (["123wronghash53453"], order_res_wrong_ingredients_hash_code, None, "с неверным хешом ингредиента"),
    ]