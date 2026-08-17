class Vehicle:

    def __init__(self,vehicle_number,brand,driver,price_per_km):
        self.vehicle_number = vehicle_number;
        self.brand = brand;
        self.driver = driver;
        self.price_per_km = price_per_km;

    def calculate_fare(self,distance):
        return distance * self.price_per_km;

    def display_details(self):
        print(f"vehicle Number: {self.vehicle_number}")
        print(f"Brand: {self.brand}")
        print(f"Driver: {self.driver}")
        print(f"Price per KM: {self.price_per_km}")
       
        