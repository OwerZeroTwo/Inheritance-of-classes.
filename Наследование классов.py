class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 800000

    def horse_powers(self):
        return 250


class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 600000

    def horse_powers(self):
        return 180



car1 = Car()
print(f"Цена автомабиля: {car1.price}")
print(f"Мощность автомобиля: {car1.horse_powers()}")

nissan1 = Nissan()
print(f"Цена Nissan: {nissan1.price}")
print(f"Мощность Nissan: {nissan1.horse_powers()}")

kia1 = Kia()
print(f"Цена Kia: {kia1.price}")
print(f"Мощность Kia: {kia1.horse_powers()}")
