#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.__age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.__age} days old ")

    def age(self) -> None:
        self.__age += 1

    def grow(self) -> None:
        self.height = round(0.8 + self.height, 1)


if __name__ == "__main__":
    p1 = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    p1.show()
    for i in range(1, 8):
        print("=== Day " + str(i) + " ===")
        p1.grow()
        p1.age()
        p1.show()

