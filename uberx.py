from carbasic import CarBasic


class UberX(CarBasic):
    def __init__(self, id, license, driver, passenger, brand, model):
        if passenger <= 4:
            super().__init__(id, license, driver, passenger, brand, model)
        else:
            raise ValueError("No se pueden montar mas de 4 pasajeros")
            # Passengers: 4