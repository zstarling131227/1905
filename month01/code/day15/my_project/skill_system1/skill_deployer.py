class Car():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Moto(Car):
    def __init__(self, brand, speed, battery_capacity, charging_power):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


# from skill_system1.skill_manager import *



