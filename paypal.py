from payment import Payment


class Paypal(Payment):
    def __init__(self, id, email):
        super().__init__(id)
        self.email = email