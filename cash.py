from payment import Payment


class Cash(Payment):

    # Constructor

    def __init__(self, id, cost):
        super().__init__(id, cost)