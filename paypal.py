from payment import Payment


class Paypal(Payment):

    # Constructor

    def __init__(self, id, cost, email):
        super().__init__(id, cost)
        self.email = email
        