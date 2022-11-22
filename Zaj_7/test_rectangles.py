import unittest
import rectangles as rect


class TestRectangle(unittest.TestCase):
    def setUp(self): pass
    def tearDown(self): pass

    def test_str(self):
        self.assertEqual(str(rect.Rectangle(1, 2, 3, 4)), '[(1, 2), (3, 4)]')
        self.assertEqual(str(rect.Rectangle(-1, -2, -3, -4)),
                         '[(-1, -2), (-3, -4)]')
        self.assertEqual(str(rect.Rectangle(-1, 2, -3, 4)),
                         '[(-1, 2), (-3, 4)]')

    def test_repr(self):
        self.assertEqual(repr(rect.Rectangle(1, 2, 3, 4)),
                         'Rectangle(1, 2, 3, 4)')
        self.assertEqual(repr(rect.Rectangle(-1, -2, -3, -4)),
                         'Rectangle(-1, -2, -3, -4)')
        self.assertEqual(repr(rect.Rectangle(-1, -2, 3, 4)),
                         'Rectangle(-1, -2, 3, 4)')

    def test_eg(self):
        self.assertEqual(rect.Rectangle(1, 2, 3, 4),
                         rect.Rectangle(1, 2, 3, 4))
        self.assertEqual(rect.Rectangle(-1, -2, -3, -4),
                         rect.Rectangle(-1, -2, -3, -4))
        self.assertEqual(rect.Rectangle(-1, -2, 3, 4),
                         rect.Rectangle(-1, -2, 3, 4))

    def test_ne(self):
        self.assertNotEqual(rect.Rectangle(1, 2, 3, 4),
                            rect.Rectangle(-1, -2, 3, 4))
        self.assertNotEqual(rect.Rectangle(-1, 2, -3, 4),
                            rect.Rectangle(1, 2, -3, -4))
        self.assertNotEqual(rect.Rectangle(-1, 2, -3, 8),
                            rect.Rectangle(-1, -2, -3, -4))

    def test_center(self):
        self.assertEqual(rect.Rectangle(1, 2, 3, 4).center(), rect.Point(2, 3))
        self.assertEqual(rect.Rectangle(-1, 1, 2, -2).center(),
                         rect.Point(0.5, -0.5))
        self.assertEqual(rect.Rectangle(
            10, 30, 50, 70).center(), rect.Point(30, 50))

    def test_area(self):
        self.assertEqual(rect.Rectangle(1, 2, 3, 4).area(),
                         rect.Rectangle(0, 0, 2, 2).area())
        self.assertEqual(rect.Rectangle(10, 10, 50, 50).area(),
                         rect.Rectangle(-10, -10, -50, -50).area())
        self.assertEqual(rect.Rectangle(-10, -10, 10, 10).area(), 400)

    def test_move(self):
        ex_rect = rect.Rectangle(0, 0, 2, 2)
        ex_rect.move(2, -2)
        self.assertEqual(ex_rect, rect.Rectangle(2, -2, 4, 0))
        ex_rect.move(-2, -2)
        self.assertEqual(ex_rect, rect.Rectangle(0, -4, 2, -2))
        ex_rect.move(10, 10)
        self.assertEqual(ex_rect, rect.Rectangle(10, 6, 12, 8))

    def test_intersection(self):
        self.assertEqual(rect.Rectangle(0, 0, 2, 2).intersection(
            rect.Rectangle(1, 1, 3, 3)), rect.Rectangle(1, 1, 2, 2))
        self.assertEqual(rect.Rectangle(0, 0, 2, 2).intersection(
            rect.Rectangle(2, 2, 4, 4)), rect.Rectangle(2, 2, 2, 2))
        with self.assertRaises(ValueError):
            rect.Rectangle(0, 0, 2, 2).intersection(rect.Rectangle(3, 3, 4, 4))

    def test_cover(self):
        self.assertEqual(rect.Rectangle(0, 0, 2, 2).cover(
            rect.Rectangle(1, 1, 3, 3)), rect.Rectangle(0, 0, 3, 3))
        self.assertEqual(rect.Rectangle(0, 0, 2, 2).cover(
            rect.Rectangle(2, 2, 4, 4)), rect.Rectangle(0, 0, 4, 4))
        self.assertEqual(rect.Rectangle(0, 0, 2, 2).cover(
            rect.Rectangle(3, 3, 4, 4)), rect.Rectangle(0, 0, 4, 4))

    def test_make4(self):
        self.assertEqual(rect.Rectangle(0, 0, 4, 4).make4(),
                         (rect.Rectangle(0, 2, 2, 4),
                          rect.Rectangle(2, 2, 4, 4),
                          rect.Rectangle(2, 0, 4, 2),
                          rect.Rectangle(0, 0, 2, 2)))
        self.assertEqual(rect.Rectangle(0, 0, 2, 2).make4(),
                         (rect.Rectangle(0, 1, 1, 2),
                          rect.Rectangle(1, 1, 2, 2),
                          rect.Rectangle(1, 0, 2, 1),
                          rect.Rectangle(0, 0, 1, 1)))
        self.assertEqual(rect.Rectangle(0, 0, 1, 1).make4(),
                         (rect.Rectangle(0, 0.5, 0.5, 1),
                          rect.Rectangle(0.5, 0.5, 1, 1),
                          rect.Rectangle(0.5, 0, 1, 0.5),
                          rect.Rectangle(0, 0, 0.5, 0.5)))


if __name__ == '__main__':
    unittest.main()
