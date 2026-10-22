#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self.set_age_days(age)
        self.set_height(height)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_days} days old ")

    def age(self) -> None:
        self._age_days += 1

    def grow(self) -> None:
        self._height = round(0.8 + self._height, 1)

    def get_height(self) -> float:
        return self._height

    def get_age_days(self) -> int:
        return self._age_days

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height cannot be negative")

    def set_age_days(self, days: int) -> None:
        if days < 0:
            print(f"{self._name}: Error, age cannot be negative")
        else:
            self._age_days = days


def main() -> None:
    print("=== Garden Security System ===")
    p = Plant("Rose", 15.0, 10)
    p.show()

    print("\nHeight updated: 25cm")
    p.set_height(25)
    print("Age updated: 30 days")
    p.set_age_days(30)
    p.show()

    print()

    p.set_height(-10.0)
    p.set_age_days(-5)
    print("Current state: ", end = "")
    p.show()



if __name__ == "__main__":
    main()
