import unittest
import points as pt


class TestPolynomials(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(pt.Point(3, 4)), "(3, 4)")
        self.assertEqual(str(pt.Point(12, 15)), "(12, 15)")
        self.assertEqual(str(pt.Point(0, 0)), "(0, 0)")

    def test_repr(self):
        self.assertEqual(repr(pt.Point(1, 1)), "Point(1, 1)")
        self.assertEqual(repr(pt.Point(-3, -8)), "Point(-3, -8)")
        self.assertEqual(repr(pt.Point(0, 0)), "Point(0, 0)")

    def test_eq(self):
        self.assertEqual(pt.Point(0, 0), pt.Point(0, 0))
        self.assertEqual(pt.Point(-18, -32), pt.Point(-18, -32))

    def test_ne(self):
        self.assertNotEqual(pt.Point(-18, -13), pt.Point(-13, -18))
        self.assertNotEqual(pt.Point(3, 2), "pt.Point(3, 2)")
        self.assertNotEqual(pt.Point(5, 5), (5, 5))

    def test_add(self):
        self.assertEqual(pt.Point(1, 1) + pt.Point(3, 3), pt.Point(4, 4))
        self.assertEqual(pt.Point(-3, -5) + pt.Point(3, 5), pt.Point(0, 0))
        self.assertNotEqual(pt.Point(-18, 1) + pt.Point(0, 0), pt.Point(0, 0))

    def test_sub(self):
        self.assertEqual(pt.Point(5, 5) - pt.Point(5, 5), pt.Point(0, 0))
        self.assertEqual(pt.Point(-2, -4) - pt.Point(-3, 5), pt.Point(1, -9))
        self.assertEqual(pt.Point(29, 2) - pt.Point(13, -2), pt.Point(16, 4))

    def test_mul(self):
        self.assertEqual(pt.Point(0, 0) * pt.Point(123, 1239), 0)
        self.assertEqual(pt.Point(2, 4) * pt.Point(3, 5), 26)
        self.assertEqual(pt.Point(-3, 2) * pt.Point(10, -100), -230)

    def test_cross(self):
        self.assertEqual(pt.Point(0, 0).cross(pt.Point(3, 4)), 0)
        self.assertEqual(pt.Point(3, 4).cross(pt.Point(3, 4)), 0)
        self.assertEqual(pt.Point(8, 5).cross(pt.Point(3, 4)), 17)

    def test_length(self):
        self.assertEqual(pt.Point(0, 0).length(), 0)
        self.assertEqual(pt.Point(30, -12).length(), 32.31098884280702)
        self.assertEqual(pt.Point(48, 9).length(), 48.83646178829912)

    def test_hash(self):
        self.assertEqual(hash(pt.Point(0, 0)), -8458139203682520985)
        self.assertEqual(hash(pt.Point(1, -1)), -6779188579744246035)
        self.assertEqual(hash(pt.Point(9, 10)), 4001662073422813760)


if __name__ == '__main__':
    unittest.main()
