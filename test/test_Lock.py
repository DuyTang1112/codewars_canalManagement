import unittest

import sys 
import os
sys.path.append(os.path.abspath(".."))

from Lock import Lock

class TestLock(unittest.TestCase):

    def setUp(self):
        self.lock = Lock(length=100, water_fill_time=10, water_empty_time=5)

    def test_initial_state(self):
        self.assertFalse(self.lock.m_isfull)
        self.assertEqual(self.lock.m_length, 100)
        self.assertEqual(self.lock.m_currentBoats, [])
        self.assertEqual(self.lock.s_waterfillTime, 10)
        self.assertEqual(self.lock.s_waterEmptyTime, 5)

    def test_setCurrentBoats(self):
        boats = ['Boat1', 'Boat2']
        processing_time = self.lock.setCurrentBoats(boats)
        self.assertEqual(self.lock.m_currentBoats, boats)

    def test_fill(self):
        fill_time = self.lock.fill()
        self.assertTrue(self.lock.m_isfull)
        self.assertEqual(fill_time, 10)

    def test_empty(self):
        self.lock.fill()  # Fill the lock first
        empty_time = self.lock.empty()
        self.assertFalse(self.lock.m_isfull)
        self.assertEqual(empty_time, 5)

if __name__ == '__main__':
    unittest.main()
