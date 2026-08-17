from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_number, brand, driver, price_per_km):
        super().__init__(vehicle_number, brand, driver, price_per_km)

    def vehicle_type(self):
        return "Car"

