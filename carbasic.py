from car import Car


class CarBasic(Car):

    # Constructor

    def __init__(self, id, license, driver, passenger, brand, model):
        super().__init__(id, license, driver, passenger)
        self.brand = brand
        self.model = model
    
    # Setters

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    # Getters

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model