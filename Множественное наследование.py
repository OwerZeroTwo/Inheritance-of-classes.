class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car():
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Внедорожник"
        self.price = 50000

    def horse_powers(self):
        return 300


nissan_car = Nissan()

print("Тип транспортного средства:", nissan_car.vehicle_type)
print("Цена:", nissan_car.price)
