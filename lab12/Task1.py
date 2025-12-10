# task1_vehicle.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Машина едет по дороге."

    def fuel_type(self):
        return "Бензин или дизель."


class Bicycle(Vehicle):
    def move(self):
        return "Велосипед движется с помощью педалей."

    def fuel_type(self):
        return "Человеческая сила (топливо не требуется)."


if __name__ == "__main__":
    car = Car()
    bike = Bicycle()

    print("Car:")
    print(" - Move:", car.move())
    print(" - Fuel:", car.fuel_type())

    print("\nBicycle:")
    print(" - Move:", bike.move())
    print(" - Fuel:", bike.fuel_type())
