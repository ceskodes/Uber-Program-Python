class Car:

    # Constructor

    def __init__(self, id, license, driver, passenger):
        self.id = id
        self.license = license
        self.driver = driver
        self.passenger = passenger

    # Propiedades (Getters, Setters)

    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    def passenger(self, passenger):
        if passenger != 4:
            raise ValueError("Pasajeros no puede ser diferente a 4")
        self._passenger = passenger