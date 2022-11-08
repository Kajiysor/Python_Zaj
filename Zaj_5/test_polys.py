import unittest
import polys as pol

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [2, 1]                   # W(x) = 2 + x
        self.p2 = [2, 1, 0]                # jw  (niejednoznaczność)
        self.p3 = [-3, 0, 1]               # W(x) = -3 + x^2
        self.p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
        self.p5 = [0]                      # zero
        self.p6 = [0, 0, 0]                # zero (niejednoznaczność)

    def test_add_poly(self):
        self.assertEqual(pol.add_poly(self.p1, self.p2), [4, 2])
        self.assertEqual(pol.add_poly(self.p2, self.p3), [-1, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(pol.sub_poly(self.p1, self.p2), [0])
        self.assertEqual(pol.sub_poly(self.p3, self.p2), [-5, -1, 1])

    def test_mul_poly(self):
        self.assertEqual(pol.mul_poly(self.p2, self.p5), [0])
        self.assertEqual(pol.mul_poly(self.p4, self.p2), [6, 3])

    def test_is_zero(self):
        self.assertTrue(pol.is_zero(self.p6))
        self.assertTrue(pol.is_zero(self.p5))
        self.assertFalse(pol.is_zero(self.p3))

    def test_eq_poly(self):
        self.assertTrue(pol.eq_poly(self.p5, self.p6))
        self.assertTrue(pol.eq_poly(self.p4, [3, 0, 0, 0]))
        self.assertTrue(pol.eq_poly(self.p1, self.p2))
        self.assertFalse(pol.eq_poly(self.p3, self.p2))

    def test_eval_poly(self):
        self.assertEqual(pol.eval_poly(self.p3, 3), 6)
        self.assertEqual(pol.eval_poly(self.p4, 30), 3)

    def test_combine_poly(self):
        self.assertEqual(pol.combine_poly(self.p1, self.p2), [4, 1])
        self.assertEqual(pol.combine_poly(self.p3, self.p4), [6])
        self.assertEqual(pol.combine_poly([16, 32, 24, 8, 1], [1, 0, 1]), [81, 0, 108, 0, 54, 0, 12, 0, 1])

    def test_pow_poly(self):
        self.assertEqual(pol.pow_poly(self.p1, 3), [8, 12, 6, 1])
        self.assertEqual(pol.pow_poly(self.p6, 13), [0])
        self.assertEqual(pol.pow_poly(self.p3, 4), [81, 0, -108, 0, 54, 0, -12, 0, 1])

    def test_diff_poly(self): 
        self.assertEqual(pol.diff_poly(self.p1), [2])
        self.assertEqual(pol.diff_poly(self.p2), [1 ,4])
        self.assertEqual(pol.diff_poly(self.p3), [0, -6])


if __name__ == '__main__':
    unittest.main()