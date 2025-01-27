class BoatQueue:
    def __init__(self, boats=[]):
        self.m_boats = boats  # The boats currently in the queue

    def getMaxBoatsToLock(self, lock):
        """
        Get the maximum number of boats that can fit in the lock
        """
        max_boats = []
        #TODO
        return max_boats

    def removeBoat(self, n):
        """
        Remove the first n boats from the queue
		"""
        removed_boats = self.m_boats[:n]
        self.m_boats = self.m_boats[n:]
        return removed_boats

    def isEmpty(self):
        return len(self.m_boats) == 0