import unittest
import a
import b

class TestThing(unittest.TestCase):
    def test_a(self):
        self.assertEqual(a.f(), 2)

    def test_b(self):
        self.assertEqual(b.g(), 3)

if __name__ == '__main__':
    unittest.main()
