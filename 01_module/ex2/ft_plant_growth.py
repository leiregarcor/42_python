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
    p1 = Plant("Rose", 25.0, 30)
    p_height = p1.height
    print("=== Garden Plant Growth ===")
    p1.show()
    for i in range(1, 8):
        print("=== Day " + str(i) + " ===")
        p1.grow()
        p1.age()
        p1.show()
    print("Growth this week: ", end="")
    print(f"{p1.height - p_height:.1f}cm")


if __name__ == "__main__":
    main()
