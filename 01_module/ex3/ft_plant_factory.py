#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old ")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height = round(0.8 + self.height, 1)


def main() -> None:
    plant_list = [
       Plant("Rose", 25.0, 30),
       Plant("Oak", 200.0, 365),
       Plant("Cactus", 5.0, 90),
       Plant("Sunflower", 80.0, 45),
       Plant("Fern", 15.5, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plant_list:
        print("Created: ", end = "")
        plant.show()


if __name__ == "__main__":
    main()
