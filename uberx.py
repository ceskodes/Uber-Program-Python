from carbasic import CarBasic


class UberX(CarBasic):
    def __init__(self, id, license, driver, passenger, brand, model):
        super().__init__(id, license, driver, passenger, brand, model)

    def get_driver(self):
        print(f'El conductor del automovil {self.brand} {self.model} es {vars(self.driver)}')