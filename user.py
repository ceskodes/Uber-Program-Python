from account import Account


class User(Account):

    # Constructor

    def __init__(self, id, name, document, email, password, trip = "Aun no ha sido asignado"):
        super().__init__(id, name, document, email, password)
        self.trip = trip

    # Setter

    def set_trip(self, trip):
        self.trip = trip