import unittest
import a
import b

class TestThing(unittest.TestCase):
    def test_a(self):
        self.assertEqual(a.f(), 1)

    def test_b(self):
        self.assertEqual(b.g(), 3)

if __name__ == '__main__':
    unittest.main()
