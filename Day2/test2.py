
import os

class Vehicle():
    def __init__(self, brand, model, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"{self.brand} {self.model} {self.rental_price_per_day}")

class Car(Vehicle):
    def __init__(self, brand, model, rental_price_per_day, seats):
        super().__init__(brand, model, rental_price_per_day)
        self.seats = seats

    def display_info(self):
        print(f"{self.brand} {self.model} {self.rental_price_per_day} {self.seats}")   

class Bike(Vehicle):
    def __init__(self, brand, model, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"{self.brand} {self.model} {self.rental_price_per_day} {self.engine_capacity}")

carobj = Car('Toyota', 2025, 4500.5, 5)
carobj.display_info()

carobj = Car('Yamaha', 2024, 1500.5, 125)
carobj.display_info()


