class Car:
    price = 1400000
    hp = 225
    def horse_power(self):
        return self.hp

class Nissan(Car):
    price = 600000
    hp = 105
    def horse_power(self):
        return self.hp

class Kia(Car):
    price = 800000
    hp = 120
    def horse_power(self):
        return self.hp

car_1 = Car()
car_1.horse_power()
print(f'Линейка наших авто имеет общую мощность в {car_1.horse_power()} лошадиных сил')

car_2 = Nissan()
car_2.horse_power()
print(f'Nissan имеет мощность в {car_2.horse_power()} лошадиных сил')

car_3 = Kia()
car_3.horse_power()
print(f'Kia имеет мощность в {car_3.horse_power()} лошадиных сил')