"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0  # разве тут тоже не надо переопределять инит?

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        if self.cargo + number <= self.max_cargo:
            self.cargo += self.cargo + number
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        new_cargo = self.cargo
        self.cargo = 0

        return new_cargo
