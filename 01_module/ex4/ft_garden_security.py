#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age_days = age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age_days} days old ")

    def age(self) -> None:
        self._age_days += 1

    def grow(self) -> None:
        self._height = round(0.8 + self._height, 1)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print("Error, height cannot be negative")

    def set_age(self, days: int) -> None:
        if days >= 0:
            self._age_days = days
        else:
            print("Error, age cannot be negative")


def main() -> None:
    print("=== Plant Factory Output ===")
    p = Plant("rose", 25, 30)
    p.show()
    p.age()
    p.grow()
    p.show()


if __name__ == "__main__":
    main()
