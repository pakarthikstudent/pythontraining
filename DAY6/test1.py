import unittest

def fx(a,b):
    return a+b
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(fx(10,20),50)


if __name__ == '__main__':
    unittest.main()
