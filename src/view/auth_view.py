
from view.app_view import AppView

class AuthView(AppView):

    def auth_menu(self):
        self.clear_screen()
        print('============ BlackJack ============')            
        print("What would you like to do?")
        print("[1] - Login")
        print("[2] - Register")
        decision_menu = input("Select an option: ")
        return decision_menu
    

    def register_form_header(self):
        self.clear_screen()
        print('============ BlackJack New Account ============')
    

    def login_form(self):
        self.clear_screen()
        print('============ BlackJack Login ============')
        
        username = input('Insert your username: ').strip()
        password = input('Insert your password: ').strip()

        return username, password


