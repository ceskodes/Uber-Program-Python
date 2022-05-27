from car import Car


class CarAdvanced(Car):
    def __init__(self, id, license, driver, passenger, typeCarAccepted, seatsMaterial):
        super().__init__(id, license, driver, passenger)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial