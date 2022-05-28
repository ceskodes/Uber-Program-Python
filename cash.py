from payment import Payment


class Cash(Payment):

    # Constructor
    
    def __init__(self, id):
        super().__init__(id)