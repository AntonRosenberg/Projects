import numpy as np

class Prisoner:
    def __init__(self, strategy: list):
        self.years = 0
        self.strategy = strategy

    def change_strategy(self):
        self.strategy = [-1 for _ in range(len(self.strategy))]

    def sentence(self, years: float):
        self.years += years


