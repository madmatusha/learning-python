#!/usr/bin/env python3

class Worker:
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.payment *= (1.0 + percent)
