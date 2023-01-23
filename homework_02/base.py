from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # weight = 20
    # started = False
    # fuel = 10
    # fuel_consumption = 9

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if self.fuel >= distance * self.fuel_consumption:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel
