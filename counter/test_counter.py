"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class CounterTest(unittest.TestCase):
    def test_Sigleton(self):
        n1 = Counter()
        n2 = Counter()
        n1.increment()
        self.assertEqual(n1, n2)



