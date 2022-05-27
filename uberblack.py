from caradvanced import CarAdvanced


class UberBlack(CarAdvanced):
    def __init__(self, id, license, driver, passenger, typeCarAccepted, seatsMaterial):
        super().__init__(id, license, driver, passenger, typeCarAccepted, seatsMaterial)
        # Passengers: 4