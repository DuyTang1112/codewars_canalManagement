import unittest
import sys
import os

sys.path.append(os.path.abspath(".."))

from Boat import Boat



class TestBoat(unittest.TestCase):

	def setUp(self):
		self.boat = Boat()

	def test_initial_state(self):
		self.assertEqual(self.boat.getLength(), 0)

	def test_set_length(self):
		self.boat.m_length = 10
		self.assertEqual(self.boat.getLength(), 10)

	def test_reset_length(self):
		self.boat.m_length = 15
		self.boat.m_length = 0
		self.assertEqual(self.boat.getLength(), 0)

if __name__ == '__main__':
	unittest.main()