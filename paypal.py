from payment import Payment


class Paypal(Payment):

    # Constructor
    
    def __init__(self, id, email):
        super().__init__(id)
        self.email = email