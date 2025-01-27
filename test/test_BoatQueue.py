import unittest
import sys 
import os
sys.path.append(os.path.abspath(".."))

from BoatQueue import BoatQueue
from Lock import Lock
from Boat import Boat

class TestBoatQueue(unittest.TestCase):

	def setUp(self):
		self.boat_queue = BoatQueue()
		self.lock = Lock(length=100, water_fill_time=10, water_empty_time=5)

	def test_getMaxBoatsToLock_empty_queue(self):
		max_boats = self.boat_queue.getMaxBoatsToLock(self.lock)
		self.assertEqual(max_boats, [])

	def test_getMaxBoatsToLock_some_boats_fit(self):
		boat1 = Boat(length=30)
		boat2 = Boat(length=40)
		boat3 = Boat(length=50)
		self.boat_queue.m_boats = [boat1, boat2, boat3]
		max_boats = self.boat_queue.getMaxBoatsToLock(self.lock)
		self.assertEqual(max_boats, [boat1, boat2])

	def test_getMaxBoatsToLock_all_boats_fit(self):
		boat1 = Boat(length=30)
		boat2 = Boat(length=20)
		boat3 = Boat(length=40)
		self.boat_queue.m_boats = [boat1, boat2, boat3]
		max_boats = self.boat_queue.getMaxBoatsToLock(self.lock)
		self.assertEqual(max_boats, [boat1, boat2, boat3])

	def test_getMaxBoatsToLock_no_boats_fit(self):
		boat1 = Boat(length=110)
		self.boat_queue.m_boats = [boat1]
		max_boats = self.boat_queue.getMaxBoatsToLock(self.lock)
		self.assertEqual(max_boats, [])

if __name__ == '__main__':
	unittest.main()