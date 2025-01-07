class User:
    def __init__(self, username, password, chips=0):
        self.__username = username
        self.__password = password
        self.__chips = chips

    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @property
    def chips(self):
        return self.__chips

    @chips.setter
    def chips(self, value):
        if not isinstance(value, int):
            raise ValueError("Chips must be an integer.")
        if value < 0:
            raise ValueError("Chips cannot be negative.")
        self.__chips = value

    def to_dict(self): 
        return {
            "username": self.__username,
            "password": self.__password,
            "total_chips": self.chips
        }
    
