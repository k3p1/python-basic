"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = None

    def set_engine(self):
        self.engine = Engine

