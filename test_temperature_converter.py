import unittest
from main import c_to_f, f_to_c, c_to_k, k_to_c, f_to_k, k_to_f

class TestTemperatureConverter(unittest.TestCase):
    def test_c_to_f(self):
        self.assertAlmostEqual(c_to_f(0), 32)
        self.assertAlmostEqual(c_to_f(100), 212)

    def test_f_to_c(self):
        self.assertAlmostEqual(f_to_c(32), 0)
        self.assertAlmostEqual(f_to_c(212), 100)

    def test_c_to_k(self):
        self.assertAlmostEqual(c_to_k(0), 273.15)
        self.assertAlmostEqual(c_to_k(-273.15), 0)

    def test_k_to_c(self):
        self.assertAlmostEqual(k_to_c(273.15), 0)
        self.assertAlmostEqual(k_to_c(0), -273.15)

    def test_f_to_k(self):
        self.assertAlmostEqual(f_to_k(32), 273.15)
        self.assertAlmostEqual(f_to_k(-459.67), 0, places=2)

    def test_k_to_f(self):
        self.assertAlmostEqual(k_to_f(273.15), 32)
        self.assertAlmostEqual(k_to_f(0), -459.67, places=2)

if __name__ == '__main__':
    unittest.main()
