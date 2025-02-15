import unittest

def add(a,b):
    return a+b
class test_add_function(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2,3),5,"Adding positive numbers resulted in wrong answer")
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2,-3),-5,"Adding negative numbers resulted in wrong answer")
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2,3),1,"Adding mixed numbers resulted in wrong answer")

if __name__ == "__main__":
    unittest.main()