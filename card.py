from payment import Payment


class Card(Payment):

    # Constructor

    def __init__(self, id, cost, number, cvv, date, bank):
        super().__init__(id, cost)
        self.number = number
        self.cvv = cvv
        self.date = date
        self.bank = bank
        