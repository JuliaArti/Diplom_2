import generators
import pytest
from src.burgers_api import BurgersAPI

API = BurgersAPI()

@pytest.fixture
def generate_user_data():
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.first_name_generator()
    create_user_body = {'email': email, 'password': password, 'name': name}
    yield [API, create_user_body]
    login_user = API.auth_user(email, password)
    if (login_user.status_code == 200):
        login_user_resp = login_user.json()
        API.delete_user(login_user_resp["accessToken"])


@pytest.fixture
def create_registred_user(generate_user_data):
    email = generate_user_data[1]["email"]
    password = generate_user_data[1]["password"]
    name = generate_user_data[1]["name"]
    registred_user_body = {'email': email, 'password': password, 'name': name}
    API.create_user(email, password, name)
    return [API, registred_user_body]  # Заменили yield на return

@pytest.fixture
def create_authenticated_user(create_registred_user):
    email = create_registred_user[1]["email"]
    password = create_registred_user[1]["password"]
    name = create_registred_user[1]["name"]
    login_user = API.auth_user(email, password)
    login_user_resp = login_user.json()
    access_token = login_user_resp["accessToken"]
    auth_user_body = {'email': email, 'password': password, 'name': name, 'access_token': access_token}
    return [API, auth_user_body]  # Заменили yield на return    