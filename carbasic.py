from car import Car


from car import Car


class CarBasic(Car):
    def __init__(self, id, license, driver, passenger, brand, model):
        super().__init__(id, license, driver, passenger)
        self.brand = brand
        self.model = model
    
    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model