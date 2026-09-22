import unittest
from billing import invoice
class T(unittest.TestCase):
    def test_basic(self):
        self.assertIn("TOTAL:30", invoice([("a", 10), ("b", 20)], round_to=1))
if __name__ == "__main__":
    unittest.main()
