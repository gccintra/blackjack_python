from controller.data_record import DataRecord
from view.auth_view import AuthView
from utils import get_valid_input
from model.user import User


class Auth():
    def __init__(self) -> None:
        self.db = DataRecord("users.json")
        self.auth_view = AuthView()

    def login(self):
        while True:
            username, password = self.auth_view.login_form()
            try:
                users = self.db.get_models()
                user = None
                for u in users:
                    if username == u["username"]:
                        user = User(u["username"], u["password"], u["total_chips"])
                        break
            except Exception as e:
                self.auth_view.display_message(f"An error occurred: {e}. Please try again.", sleep_time=4)
                continue

            if user and user.password == password:
                self.auth_view.display_message("Login successful!", sleep_time=2)
                return user
            else:
                self.auth_view.display_message("Incorrect username or password.", sleep_time=2)

 
     
    def register(self):
        self.auth_view.register_form_header()

        username = get_valid_input(
            'Username: ',
            [
                (lambda x: len(x) >= 3, "Username must have at least 3 characters."),
                (lambda x: x not in [model['username'] for model in self.db.get_models()], "There is already a user with that username.")
            ]
        )

        password = get_valid_input(
                'Password: ',
                [
                    (lambda x: len(x) >= 8, "Password must have at least 8 characters."),
                    (lambda x: any(char.islower() for char in x), "Password must contain at least one lowercase letter."),
                    (lambda x: any(char.isupper() for char in x), "Password must contain at least one uppercase letter."),
                    (lambda x: any(char.isdigit() for char in x), "Password must contain at least one number."),
                    (lambda x: any(char in """!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~""" for char in x),
                    "Password must contain at least one special character.")
                ]
            )

        new_user = User(username, password)
        new_user_dict = new_user.to_dict()
        if self.db.write(new_user_dict):
            self.auth_view.display_message(f"User '{username}' registered successfully!", sleep_time=2)
        else:
            self.auth_view.display_message("An error occurred while creating the user. Please try again.", sleep_time=2)
            del new_user
        

