from abc import ABC


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 10
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = 0
        self.fuel = 0
        self.fuel_consumption = 0

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
