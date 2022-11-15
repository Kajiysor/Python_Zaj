from __future__ import annotations
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self) -> str:                      # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self) -> str:                     # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other: Rectangle) -> bool:    # obsługa rect1 == rect2
        return isinstance(other, Rectangle) and self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other: Rectangle) -> bool:    # obsługa rect1 != rect2
        return not self == other

    def center(self) -> Point:                     # zwraca środek prostokąta
        return Point((self.pt1 + self.pt2).x / 2, (self.pt1 + self.pt2).y / 2)

    def area(self) -> float:                       # pole powierzchni
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    def move(self, x: float, y: float) -> None:    # przesunięcie o (x, y)
        move_pt = Point(x, y)
        self.pt1, self.pt2 = self.pt1 + move_pt, self.pt2 + move_pt
