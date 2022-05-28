from account import Account


class Driver(Account):
    def __init__(self, id, name, document, email, password):
        super().__init__(id, name, document, email, password)

    def get_driver(self):
        print(f'El conductor asignado para el servicio: {self.name} y su identificacion es {self.document}.')