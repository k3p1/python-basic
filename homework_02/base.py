from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # weight = 20
    # started = False
    # fuel = 10
    # fuel_consumption = 9  # Мне кажется тут атрибуты не нужны, мы же их дальше переопределяем.

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        # нужна ли тут проверка fuel_consumption > 0, и как можно ли тут делать её, это отдельное исключение выходит
        self.fuel_consumption = fuel_consumption
        self.started = False  # может тут лучше None поставить? значения же по факту нет

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if self.fuel >= distance * self.fuel_consumption:  # нужна ли проверка distance, fuel >= 0
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel
