from caradvanced import CarAdvanced


class UberVan(CarAdvanced):
    def __init__(self, id, license, driver, passenger, typeCarAccepted, seatsMaterial):
        super().__init__(id, license, driver, passenger, typeCarAccepted, seatsMaterial)
    
    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    def passenger(self, passenger):
        if passenger != 6:
            raise ValueError("Pasajeros no puede ser diferente a 6")
        self._passenger = passenger