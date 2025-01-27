import unittest
import sys
import os

sys.path.append(os.path.abspath(".."))

from Canal import Canal
from Lock import Lock
from BoatQueue import BoatQueue
from Boat import Boat


class TestCanal(unittest.TestCase):

	def setUp(self):
		self.lock = Lock(length=7, water_fill_time=2, water_empty_time=2)
		self.low_queue = BoatQueue()
		self.high_queue = BoatQueue()
		self.canal = Canal(self.lock, self.low_queue, self.high_queue)

	def test_initial_state(self):
		self.assertEqual(self.canal.m_Lock, self.lock)
		self.assertEqual(self.canal.m_lowQueue, self.low_queue)
		self.assertEqual(self.canal.m_highQueue, self.high_queue)

	def test_process_empty_queues(self):
		total_time = self.canal.process()
		self.assertEqual(total_time, 0)	
	
	def test_process_example(self):
		boat1 = Boat(length=2)
		boat2 = Boat(length=3)
		boat3 = Boat(length=6)
		boat4 = Boat(length=1)
		boat5 = Boat(length=1)
		boat6 = Boat(length=2)

		self.low_queue.m_boats = [boat1, boat2, boat3, boat4]
		self.high_queue.m_boats = [boat5, boat6]

		total_time = self.canal.process()
		self.assertEqual(total_time, 38)
if __name__ == '__main__':
	unittest.main()