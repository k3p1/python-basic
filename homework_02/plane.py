"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cargo = 10
        self.max_cargo = 100

    def load_cargo(self, num):
        if self.cargo + num <= self.max_cargo:
            self.cargo += num
        else:
            raise CargoOverload

    # def remove_all_cargo(self):
    #     self.cargo = super(self.cargo)