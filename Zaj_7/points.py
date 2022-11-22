from __future__ import annotations


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x: float, y: float):                      # konstuktor
        self.x = x
        self.y = y

    def __str__(self) -> str:                      # zwraca string "(x, y)"
        return (f"({self.x}, {self.y})")

    def __repr__(self) -> str:                     # zwraca string "Point(x, y)"
        return (f"Point({self.x}, {self.y})")

    def __eq__(self, other: Point) -> bool:        # obsługa point1 == point2
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __ne__(self, other: Point) -> bool:        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other: Point) -> Point:      # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:      # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Point) -> float:      # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other: Point) -> float:        # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self) -> float:                     # długość wektora
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    def __hash__(self) -> int:                     # bazujemy na tuple, immutable points
        return hash((self.x, self.y))
