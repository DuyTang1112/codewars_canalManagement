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
		self.lock = Lock(length=7, water_fill_time=2, water_empty_time=2)

		self.low_queue.m_boats = [Boat(2), Boat(3), Boat(6), Boat(1)]
		self.high_queue.m_boats = [Boat(1), Boat(2)]
		self.canal = Canal(self.lock, self.low_queue, self.high_queue)

		total_time = self.canal.process()
		self.assertEqual(total_time, 38)
		
	def test_process_example2(self):
		self.lock = Lock(length=8, water_fill_time=2, water_empty_time=2)
		self.low_queue.m_boats = [Boat(4), Boat(1), Boat(8), Boat(2), Boat(6)]
		self.high_queue.m_boats = []
		self.canal = Canal(self.lock, self.low_queue, self.high_queue)

		total_time = self.canal.process()
		self.assertEqual(total_time, 54)
		
	def test_process_example3(self):
		self.lock = Lock(length=8, water_fill_time=2, water_empty_time=2)
		self.low_queue.m_boats = []
		self.high_queue.m_boats = [Boat(4), Boat(4), Boat(7), Boat(2), Boat(8), Boat(5)]
		self.canal = Canal(self.lock, self.low_queue, self.high_queue)

		total_time = self.canal.process()
		self.assertEqual(total_time, 80)
		
	def test_process_example4(self):
		self.lock = Lock(length=10, water_fill_time=2, water_empty_time=2)
		self.low_queue.m_boats = []
		self.high_queue.m_boats = []
		self.canal = Canal(self.lock, self.low_queue, self.high_queue)

		total_time = self.canal.process()
		self.assertEqual(total_time, 0)
		
	def test_process_example5(self):
		self.lock = Lock(length=30, water_fill_time=2, water_empty_time=2)
		self.low_queue.m_boats = [Boat(1), Boat(2), Boat(3), Boat(4), Boat(5), Boat(7), Boat(8), Boat(9), Boat(10), Boat(11), Boat(12), Boat(13), Boat(14), Boat(15), Boat(16), Boat(17), Boat(18), Boat(19), Boat(20)]
		self.high_queue.m_boats = [Boat(20), Boat(19), Boat(18), Boat(17), Boat(16), Boat(15), Boat(14), Boat(13), Boat(12), Boat(11), Boat(10), Boat(9), Boat(8), Boat(7), Boat(6), Boat(5), Boat(4), Boat(3), Boat(2), Boat(1)]
		self.canal = Canal(self.lock, self.low_queue, self.high_queue)

		total_time = self.canal.process()
		self.assertEqual(total_time, 868)
		

if __name__ == '__main__':
	unittest.main()