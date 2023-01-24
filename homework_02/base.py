from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=10, fuel=10, fuel_consumption=2):
        # if weight or fuel or fuel_consumption >= 0:
        #     self.weight = weight
        #     self.fuel = fuel
        #     self.fuel_consumption = fuel_consumption
        # else:
        #     raise ValueError
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
        # if distance >= 0:
        #     if self.fuel >= distance * self.fuel_consumption:
        #         self.fuel -= distance * self.fuel_consumption
        #     else:
        #         raise NotEnoughFuel
        # else:
        #     raise ValueError
        if self.fuel >= distance * self.fuel_consumption:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel
