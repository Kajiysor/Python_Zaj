from __future__ import annotations
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, pt1: Point, pt2: Point) -> Rectangle:
        if not (isinstance(pt1, Point) and isinstance(pt2, Point)):
            raise TypeError("pt1 and pt2 must be Point")
        return cls(pt1.x, pt1.y, pt2.x, pt2.y)

    def __str__(self) -> str:                               # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self) -> str:                              # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other: Rectangle) -> bool:             # obsługa rect1 == rect2
        return isinstance(other, Rectangle) and self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other: Rectangle) -> bool:             # obsługa rect1 != rect2
        return not self == other

    @property
    def center(self) -> Point:                              # zwraca środek prostokąta
        return Point((self.pt1 + self.pt2).x / 2, (self.pt1 + self.pt2).y / 2)

    @property
    def area(self) -> float:                                # pole powierzchni
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    @property
    def top(self) -> float:
        return self.pt2.y

    @property
    def bottom(self) -> float:
        return self.pt1.y
    
    @property
    def left(self) -> float:
        return self.pt1.x
    
    @property
    def right(self) -> float:
        return self.pt2.x
    
    @property
    def width(self) -> float:
        return abs(self.pt2.x - self.pt1.x)
    
    @property
    def height(self) -> float:
        return abs(self.pt2.y - self.pt1.y)

    @property
    def top_left(self) -> Point:
        return Point(self.pt1.x, self.pt2.y)

    @property
    def top_right(self) -> Point:
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottom_left(self) -> Point:
        return Point(self.pt1.x, self.pt1.y)

    @property
    def bottom_right(self) -> Point:
        return Point(self.pt2.x, self.pt1.y)

    def move(self, x: float, y: float) -> None:             # przesunięcie o (x, y)
        move_pt = Point(x, y)
        self.pt1, self.pt2 = self.pt1 + move_pt, self.pt2 + move_pt

    def intersection(self, other: Rectangle) -> Rectangle:  # część wspólna prostokątów
        if not isinstance(other, Rectangle):
            raise TypeError("Other must be Rectangle")
        if self.pt1.x > other.pt2.x or self.pt2.x < other.pt1.x or self.pt1.y > other.pt2.y or self.pt2.y < other.pt1.y:
            raise ValueError("No intersection")
        else:
            return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other: Rectangle) -> Rectangle:         # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise TypeError("Other must be Rectangle")
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self) -> tuple:                               # zwraca krotkę czterech mniejszych
        return (
            Rectangle(self.pt1.x, self.center().y,
                      self.center().x, self.pt2.y),
            Rectangle(self.center().x, self.center().y,
                      self.pt2.x, self.pt2.y),
            Rectangle(self.center().x, self.pt1.y,
                      self.pt2.x, self.center().y),
            Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y))

