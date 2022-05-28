from account import Account


class Driver(Account):

    # Constructor

    def __init__(self, id, name, document, email, password):
        super().__init__(id, name, document, email, password)