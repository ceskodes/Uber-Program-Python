from carbasic import CarBasic


class UberPool(CarBasic):

    # Constructor
    
    def __init__(self, id, license, driver, passenger, brand, model):
        super().__init__(id, license, driver, passenger, brand, model)