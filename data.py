class Url:
    BASE_URL = 'https://stellarburgers.education-services.ru'
    CREATE_USER = "/api/auth/register"
    AUTH_USER = "/api/auth/login"
    DELETE_USER = "/api/auth/user"
    ORDERS_ENDPOINT = "/api/orders"
    IMGREDIENTS_ENDPOINT = "/api/ingredients"

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